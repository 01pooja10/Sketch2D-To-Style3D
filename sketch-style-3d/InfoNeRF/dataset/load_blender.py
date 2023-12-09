import os
import torch
import numpy as np
import imageio 
import json
import torch.nn.functional as F
import cv2
from tqdm import tqdm 

trans_t = lambda t : torch.Tensor([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,t],
    [0,0,0,1]]).float()

rot_phi = lambda phi : torch.Tensor([
    [1,0,0,0],
    [0,np.cos(phi),-np.sin(phi),0],
    [0,np.sin(phi), np.cos(phi),0],
    [0,0,0,1]]).float()

rot_theta = lambda th : torch.Tensor([
    [np.cos(th),0,-np.sin(th),0],
    [0,1,0,0],
    [np.sin(th),0, np.cos(th),0],
    [0,0,0,1]]).float()


def pose_spherical(theta, phi, radius):
    c2w = trans_t(radius)
    c2w = rot_phi(phi/180.*np.pi) @ c2w
    c2w = rot_theta(theta/180.*np.pi) @ c2w
    c2w = torch.Tensor(np.array([[-1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])) @ c2w
    return c2w


def load_blender_data(basedir, half_res=False, testskip=1):
    splits = ['train', 'val', 'test']

    metas = {}
    for s in splits:
        with open(os.path.join(basedir, 'transforms_{}.json'.format(s)), 'r') as fp:
            metas[s] = json.load(fp)

    all_imgs = []
    all_poses = []
    counts = [0]
    for s in splits:
        meta = metas[s]
        imgs = []
        poses = []
        if s=='train' or testskip==0:
            skip = 1
        else:
            skip = testskip
            
        for frame in meta['frames'][::skip]:
            fname = os.path.join(basedir, frame['file_path'] + '.png')
            imgs.append(imageio.imread(fname))
            poses.append(np.array(frame['transform_matrix'])) 
        imgs = (np.array(imgs) / 255.).astype(np.float32) # keep all 4 channels (RGBA)
        poses = np.array(poses).astype(np.float32)
        counts.append(counts[-1] + imgs.shape[0])
        all_imgs.append(imgs)
        all_poses.append(poses) 

    all_masks = []
    if os.path.exists(os.path.join(basedir, 'transforms_mask.json')):
        with open(os.path.join(basedir, 'transforms_mask.json'), 'r') as fp:
            meta = json.load(fp)

        imgs = []    
        for frame in meta['frames'][::1]:
            fname = os.path.join(basedir, frame['file_path'] + '.png')
            imgs.append(imageio.imread(fname))
        imgs = np.array(imgs).astype(np.float32) # Greyscale image with [0,1] values 
        counts.append(counts[-1] + imgs.shape[0])
        all_masks.append(imgs)

    
    i_split = [np.arange(counts[i], counts[i+1]) for i in range(3)]
    
    # Eliminate alpha channel if necessary 
    for i, img in enumerate(all_imgs): 
        print(img.shape)
        if img.shape[-1] == 4: 
            all_imgs[i] = img[...,:3]

    target_height, target_width = all_imgs[0][0,...].shape[:2] # Get the height and width of the target size
    resized_imgs = np.zeros(shape=(all_imgs[2].shape[0], target_width, target_height, all_imgs[0].shape[3]))
    for img_idx in range(all_imgs[2].shape[0]):
        resized_imgs[img_idx,...] = cv2.resize(all_imgs[2][img_idx,...], (target_width, target_height)) # Resize images
    all_imgs[2] = resized_imgs

    imgs = np.concatenate(all_imgs, 0)
    poses = np.concatenate(all_poses, 0)

    if all_masks != []: 
        masks = np.concatenate(all_masks, 0) 
        imgs[:masks.shape[0],...] = imgs[:masks.shape[0],...] * (1 - masks[...,None]) + np.ones_like(imgs[:masks.shape[0],...]) * masks[...,None]

        ###########################################################

        test_dir = './sanity_check/' 

        if not os.path.exists(test_dir): os.mkdir(test_dir) 

        print("Saving masked images for sanity check.")
        for i in tqdm(range(imgs.shape[0])):
            test_masked_img_name = f'test_img_{i}.png'
            test_save_path_maksed_img = os.path.join(test_dir, test_masked_img_name)
            imageio.imwrite(test_save_path_maksed_img, (255 * np.clip(imgs[i], 0.0, 1.0)).astype(np.uint8))

        ###########################################################

    H, W = imgs[0].shape[:2]
    camera_angle_x = float(meta['camera_angle_x'])
    focal = .5 * W / np.tan(.5 * camera_angle_x)
    
    render_poses = torch.stack([pose_spherical(angle, -30.0, 4.0) for angle in np.linspace(-180,180,40+1)[:-1]], 0)
    
    if half_res:
        H = H//2
        W = W//2
        focal = focal/2.

        imgs_half_res = np.zeros((imgs.shape[0], H, W, 4))
        for i, img in enumerate(imgs):
            imgs_half_res[i] = cv2.resize(img, (W, H), interpolation=cv2.INTER_AREA)
        imgs = imgs_half_res
        # imgs = tf.image.resize_area(imgs, [400, 400]).numpy()

        
    return imgs, poses, render_poses, [H, W, focal], i_split


