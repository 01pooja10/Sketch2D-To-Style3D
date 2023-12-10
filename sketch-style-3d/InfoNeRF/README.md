This directory was adapted from the following repository: https://github.com/mjmjeong/InfoNeRF

Modifications were made to the dataset/load_blender.py file in the following lines:

https://github.com/01pooja10/Sketch2D-To-Style3D/blob/2f19522d0dbc4750c6e04c5a87ebe5a9e509d91c/sketch-style-3d/InfoNeRF/dataset/load_blender.py#L67C4-L114


With the main goal being to eliminate mis-shaping errors that may happen between training and testing elements of our dataset and to apply the makss provided. 

To run this code and obtain our results, you must the following directory from the google drive linked: InfoNeRF Datasets/nerf_synthetic 

To enter this directory here, create a directory named data and copy the nerf_synthetic directory there. 

### Quick Start 

To train a InfoNeRF on the example `lego` scene:
```
python run_nerf.py --config configs/infonerf/synthetic/lego.txt
```

To train a NeRF (baseline) on the example `lego` scene:
```
python run_nerf.py --config configs/nerf/synthetic/lego.txt
```
