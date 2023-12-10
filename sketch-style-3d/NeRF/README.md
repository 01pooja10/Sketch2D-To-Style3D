# NeRF-pytorch
This is the folder containing the code files and other dependencies to train a NeRF in PyTorch from scratch. The code files have been adapted from https://github.com/yenchenlin/nerf-pytorch

Some of the modified files are given below for reference:
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/c7339f5f688b74f931020936e1dc6938282cdb68/sketch-style-3d/NeRF/load_blender.py#L37
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/c7339f5f688b74f931020936e1dc6938282cdb68/sketch-style-3d/NeRF/load_blender.py#L58
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/c7339f5f688b74f931020936e1dc6938282cdb68/sketch-style-3d/NeRF/run_nerf.py#L525
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/c7339f5f688b74f931020936e1dc6938282cdb68/sketch-style-3d/NeRF/run_nerf.py#L535

## Data
To download a sample dataset such as the synthetic Lego NeRF data, run the following:
'''
bash download_example_data.sh
'''

To use a custom dataset (stylized images/sketches) firstly create a new folder inside the NeRF directory:
-> ./data/nerf_synthetic/
- Add train, val, and test folders with the respective images. Ensure that the order of images and nomenclature is the same as the original dataset.
- Add the necessary JSON files for train, val, and test.

## Training
To train please run:
```
python run_nerf.py --config configs/lego.txt
``` 
## Sample results

After stylizing using the first style image, the output rendered from NeRF is attached below:


https://github.com/01pooja10/Sketch2D-To-Style3D/assets/66198904/a632b0be-f2ad-49b9-8d20-d59786180ea7


After stylizing using the second style image, the output rendered from NeRF is attached below:


https://github.com/01pooja10/Sketch2D-To-Style3D/assets/66198904/91aaca0b-e959-4313-9efc-14d989b1b14e


## Citation
Cite the authors of the original NeRF paper:
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

If you find this implementation helpful, please cite:
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
