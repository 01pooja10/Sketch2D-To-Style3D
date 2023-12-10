# NeRF-pytorch
Code adapted from https://github.com/yenchenlin/nerf-pytorch

The files modified are in run_nerf.py, run_nerf_helpers.py and configs/lego.txt files. 
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/c7339f5f688b74f931020936e1dc6938282cdb68/sketch-style-3d/NeRF/load_blender.py#L37
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/c7339f5f688b74f931020936e1dc6938282cdb68/sketch-style-3d/NeRF/load_blender.py#L58
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/c7339f5f688b74f931020936e1dc6938282cdb68/sketch-style-3d/NeRF/run_nerf.py#L525
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/c7339f5f688b74f931020936e1dc6938282cdb68/sketch-style-3d/NeRF/run_nerf.py#L535

To train please run:
```
python run_nerf.py --config configs/lego.txt
``` 
## Sample results

After stylizing using the first style image, the output rendered from NeRF is attached below.
https://github.com/01pooja10/Sketch2D-To-Style3D/assets/66198904/7e27cb3f-14ec-4fdb-95bb-2a231926209a

After stylizing using the second style image, the output rendered from NeRF is attached below.
https://github.com/01pooja10/Sketch2D-To-Style3D/assets/66198904/d84b10a1-efab-4027-b7ae-412e36f18817


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
