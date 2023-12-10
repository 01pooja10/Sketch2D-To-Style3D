# ColorNerf
This code is adapted from: https://github.com/cassiePython/CLIPNeRF

Editing color of a single nerf model.

This project is built upon a [PyTorch implementation](https://github.com/yenchenlin/nerf-pytorch).

Files modified:
load_blender.py, run_nerf_clip.py, configs/lego.txt
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/0bdd7dbd60ad98747f024ba344cc8ce8a5ed7341/sketch-to-3d/CLIP-NeRF/load_blender.py#L106
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/0bdd7dbd60ad98747f024ba344cc8ce8a5ed7341/sketch-to-3d/CLIP-NeRF/run_nerf_clip.py#L1063

## Run

To train please run
```
python run_nerf_clip.py --config configs/lego.txt --use_clip --w_clip 1.5 --use_alpha --use_feature --use_view --sample_scale 128 --description "A Red Lego Excavator" 
```

Ensure that you put the pretrained nerf model from nerf-pytorch repository into logs/blender_paper_lego


|  Parameter  | Discription  |
|  ----  | ----  |
| --description  | Text prompt |
| --use_clip  | Use CLIP loss to finetune Nerf |
| --w_clip | Weight for CLIP loss |
| --use_alpha | Whether finetune alpha layers |
| --use_feature | Whether finetune feature layers |
| --use_view | Whether finetune view layers |
| --sample_scale | Patch size (the larger, the better, you can set a max value according to your GPU |

## Sample Output
https://github.com/01pooja10/Sketch2D-To-Style3D/assets/30786246/07e72dab-0764-4220-abe8-f5e54fd7686c

Sketch -> "A Red Lego Excavator"

https://github.com/01pooja10/Sketch2D-To-Style3D/assets/30786246/77511dff-a97e-45c3-bafe-cb95cf581d52

Sketch -> Colour Filled -> "A Blue Excavator"

https://github.com/01pooja10/Sketch2D-To-Style3D/assets/30786246/fe72cf09-837d-4d6f-90ae-2e0fbccc4211

Sketch -> "A Green Excavator"

https://github.com/01pooja10/Sketch2D-To-Style3D/assets/30786246/7ab8a359-0e10-4e08-9458-da84912ce58b

Sketch -> Colour Filled -> "A Red Lego Excavator" (Original CLIP-NeRF)

https://github.com/01pooja10/Sketch2D-To-Style3D/assets/30786246/f8f0c323-d0a4-4f98-acf8-466157aa5f71

Sketch -> Colour Filled -> "A Red Lego Excavator" (CLIP-NeRF with Edge Loss)

## Citation
If you use this work, please cite the original paper and its authors:
```
@misc{wang2022clipnerf,
      title={CLIP-NeRF: Text-and-Image Driven Manipulation of Neural Radiance Fields}, 
      author={Can Wang and Menglei Chai and Mingming He and Dongdong Chen and Jing Liao},
      year={2022},
      eprint={2112.05139},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
