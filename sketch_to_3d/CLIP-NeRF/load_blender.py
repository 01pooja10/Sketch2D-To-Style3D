import os
import torch
import numpy as np
import imageio
import json
import torch.nn.functional as F
import cv2
import glob

trans_t = lambda t: torch.Tensor(
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, t], [0, 0, 0, 1]]
).float()

rot_phi = lambda phi: torch.Tensor(
    [
        [1, 0, 0, 0],
        [0, np.cos(phi), -np.sin(phi), 0],
        [0, np.sin(phi), np.cos(phi), 0],
        [0, 0, 0, 1],
    ]
).float()

rot_theta = lambda th: torch.Tensor(
    [
        [np.cos(th), 0, -np.sin(th), 0],
        [0, 1, 0, 0],
        [np.sin(th), 0, np.cos(th), 0],
        [0, 0, 0, 1],
    ]
).float()


def pose_spherical(theta, phi, radius):
    c2w = trans_t(radius)
    c2w = rot_phi(phi / 180.0 * np.pi) @ c2w
    c2w = rot_theta(theta / 180.0 * np.pi) @ c2w
    c2w = (
        torch.Tensor(
            np.array([[-1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
        )
        @ c2w
    )
    return c2w


def load_blender_data(basedir, half_res=False, testskip=1):
    splits = ["train", "val", "test"]
    metas = {}
    for s in splits:
        with open(os.path.join(basedir, "transforms_{}.json".format(s)), "r") as fp:
            metas[s] = json.load(fp)

    all_imgs = []
    all_poses = []
    counts = [0]
    masks = []
    for s in splits:
        meta = metas[s]
        imgs = []
        poses = []
        if s == "train" or testskip == 0:
            skip = 1
        else:
            skip = testskip

        for frame in meta["frames"][::skip]:
            fname = os.path.join(basedir, frame["file_path"] + ".png")
            imgs.append(imageio.imread(fname, pilmode="RGBA"))
            poses.append(np.array(frame["transform_matrix"]))
        imgs = (np.array(imgs) / 255.0).astype(np.float32)  # keep all 4 channels (RGBA)
        poses = np.array(poses).astype(np.float32)
        counts.append(counts[-1] + imgs.shape[0])
        all_imgs.append(imgs)
        all_poses.append(poses)

    for mask in sorted(glob.glob(os.path.join(basedir, "mask/*.png")), key=len):
        masks.append(imageio.imread(mask, pilmode="L"))

    i_split = [np.arange(counts[i], counts[i + 1]) for i in range(3)]

    imgs = np.concatenate(all_imgs, 0)
    poses = np.concatenate(all_poses, 0)

    H, W = imgs[0].shape[:2]
    camera_angle_x = float(meta["camera_angle_x"])
    focal = 0.5 * W / np.tan(0.5 * camera_angle_x)

    render_poses = torch.stack(
        [
            pose_spherical(angle, -30.0, 4.0)
            for angle in np.linspace(-180, 180, 40 + 1)[:-1]
        ],
        0,
    )

    if half_res:
        H = H // 2
        W = W // 2
        focal = focal / 2.0

        imgs_half_res = np.zeros((imgs.shape[0], H, W, 4))
        for i, img in enumerate(imgs):
            imgs_half_res[i] = cv2.resize(img, (W, H), interpolation=cv2.INTER_AREA)
        imgs = imgs_half_res
        masks_half_res = []
        for mask in masks:
            masks_half_res.append(
                cv2.resize(mask, (W, H), interpolation=cv2.INTER_NEAREST)
            )
        masks = masks_half_res
        # imgs = tf.image.resize_area(imgs, [400, 400]).numpy()

    return (
        imgs,
        poses,
        render_poses,
        [H, W, focal],
        i_split,
        np.expand_dims(np.array(masks), -1).astype(bool),
    )


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from run_nerf_clip import get_select_inds
    import kornia

    imgs, poses, render, a, split, masks = load_blender_data(
        "./legopidi", half_res=True
    )
    imgs = torch.Tensor(imgs)
    masks = torch.Tensor(masks)
    imgs = imgs[..., :3]
    print(imgs[0].shape)

    indices = get_select_inds(64 * 64, 5000)

    target_s = torch.nn.functional.grid_sample(
        imgs[0].permute(2, 0, 1).unsqueeze(0),
        indices.unsqueeze(0),
        mode="bilinear",
        align_corners=True,
    )[0]

    mask_s = torch.nn.functional.grid_sample(
        masks[0].permute(2, 0, 1).unsqueeze(0),
        indices.unsqueeze(0),
        mode="nearest",
        align_corners=True,
    )[0]

    target_s = kornia.color.rgb_to_grayscale(target_s)
    print(target_s.shape)
    print(mask_s.shape)
    plt.imshow(torch.squeeze(target_s))
    plt.colorbar()
    plt.show()
    plt.imshow(torch.squeeze(mask_s))
    plt.colorbar()
    plt.show()
    plt.imshow((torch.squeeze(torch.bitwise_or(target_s > 0.7, mask_s.bool()))).float())
    plt.colorbar()
    plt.show()
