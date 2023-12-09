import torch
import clip


class DirectionLoss(torch.nn.Module):
    def __init__(self, loss_type="mse"):
        super(DirectionLoss, self).__init__()

        self.loss_type = loss_type

        self.loss_func = {
            "mse": torch.nn.MSELoss,
            "cosine": torch.nn.CosineSimilarity,
            "mae": torch.nn.L1Loss,
        }[loss_type]()

    def forward(self, x, y):
        if self.loss_type == "cosine":
            return 1.0 - self.loss_func(x, y)

        return self.loss_func(x, y)


class CLIPLoss(torch.nn.Module):
    def __init__(self):
        super(CLIPLoss, self).__init__()
        self.model, self.preprocess = clip.load("ViT-B/32", device="cuda")
        self.direction_loss = DirectionLoss("cosine")
        # self.upsample = torch.nn.Upsample(scale_factor=7)
        # self.avg_pool = torch.nn.AvgPool2d(kernel_size=opts.stylegan_size // 32)

    # def forward(self, gen_image, tgt_image, tgt_text, src_text):
    #     gen_image = torch.nn.functional.upsample(gen_image, (224, 224), mode="bicubic")
    #     tgt_image = torch.nn.functional.upsample(tgt_image, (224, 224), mode="bicubic")
    #     # image = self.avg_pool(self.upsample(image))
    #     gen_image_features = self.model.encode_image(gen_image)
    #     tgt_image_features = self.model.encode_image(tgt_image)

    #     gen_image_features /= gen_image_features.clone().norm(dim=-1, keepdim=True)
    #     tgt_image_features /= tgt_image_features.clone().norm(dim=-1, keepdim=True)

    #     tgt_text_features = self.model.encode_text(tgt_text).detach()
    #     src_text_features = self.model.encode_text(src_text).detach()

    #     tgt_text_features /= tgt_text_features.norm(dim=-1, keepdim=True)
    #     src_text_features /= src_text_features.norm(dim=-1, keepdim=True)

    #     txt_direction = (tgt_text_features - src_text_features).mean(
    #         axis=0, keepdim=True
    #     )
    #     txt_direction /= txt_direction.norm(dim=-1, keepdim=True)

    #     image_direction = tgt_image_features - gen_image_features
    #     image_direction /= image_direction.clone().norm(dim=-1, keepdim=True)

    #     return self.direction_loss(image_direction, txt_direction).mean()

    def forward(self, image, text):
        image = torch.nn.functional.upsample_bilinear(image, (224, 224))
        # image = self.avg_pool(self.upsample(image))
        similarity = 1 - self.model(image, text)[0] / 100
        return similarity  # .mean()
