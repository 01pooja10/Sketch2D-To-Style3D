# NeRF-pytorch
Code adapted from https://github.com/yenchenlin/nerf-pytorch

The files modified are in run_nerf.py, run_nerf_helpers.py and configs/lego.txt files. 
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/a93c3bbb4e9f17ac66ae536aaad461e2d8a8a0d8/sketch-to-3d/nerf-pytorch/run_nerf.py#L475
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/a93c3bbb4e9f17ac66ae536aaad461e2d8a8a0d8/sketch-to-3d/nerf-pytorch/run_nerf.py#L998
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/a93c3bbb4e9f17ac66ae536aaad461e2d8a8a0d8/sketch-to-3d/nerf-pytorch/run_nerf_helpers.py#L15
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/a93c3bbb4e9f17ac66ae536aaad461e2d8a8a0d8/sketch-to-3d/nerf-pytorch/run_nerf_helpers.py#L30

Please download the dataset from the google drive link: https://drive.google.com/drive/folders/1mT1Hh4cCeEca2rt1IW_Ug241jBbsKGEd?usp=share_link and place it in this directory. Modify configs/lego.txt to point towards the directory.

To train please run:
```
python run_nerf.py --config configs/lego.txt
``` 
## Sample Output
https://github.com/01pooja10/Sketch2D-To-Style3D/assets/30786246/ed06d704-a7e7-4e91-9d4e-6655dde619e5

https://github.com/01pooja10/Sketch2D-To-Style3D/assets/30786246/67062bfb-9c45-499c-8298-3a7e2b774e6e

## Citation
Kudos to the authors for their amazing results:
```
@misc{mildenhall2020nerf,
    title={NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis},
    author={Ben Mildenhall and Pratul P. Srinivasan and Matthew Tancik and Jonathan T. Barron and Ravi Ramamoorthi and Ren Ng},
    year={2020},
    eprint={2003.08934},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```

However, if you find this implementation or pre-trained models helpful, please consider to cite:
```
@misc{lin2020nerfpytorch,
  title={NeRF-pytorch},
  author={Yen-Chen, Lin},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished={\url{https://github.com/yenchenlin/nerf-pytorch/}},
  year={2020}
}
```
