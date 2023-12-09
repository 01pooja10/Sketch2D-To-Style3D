# ColorNerf
This code is adapted from: https://github.com/cassiePython/CLIPNeRF

Editing color of a single nerf model.

This project is built upon a [PyTorch implementation](https://github.com/yenchenlin/nerf-pytorch).

## Run

To train please run
```
python run_nerf_clip.py --config configs/lego.txt --use_clip --w_clip 1.5 --use_alpha --use_feature --use_view --sample_scale 128 --description "A Red Lego Excavator" 
```

|  Parameter  | Discription  |
|  ----  | ----  |
| --description  | Text prompt |
| --use_clip  | Use CLIP loss to finetune Nerf |
| --w_clip | Weight for CLIP loss |
| --use_alpha | Whether finetune alpha layers |
| --use_feature | Whether finetune feature layers |
| --use_view | Whether finetune view layers |
| --sample_scale | Patch size (the larger, the better, you can set a max value according to your GPU |
