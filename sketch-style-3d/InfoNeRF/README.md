This directory was adapted from the following repository: https://github.com/mjmjeong/InfoNeRF

Modifications were made to the dataset/load_blender.py file in the following lines:

https://github.com/01pooja10/Sketch2D-To-Style3D/blob/2f19522d0dbc4750c6e04c5a87ebe5a9e509d91c/sketch-style-3d/InfoNeRF/dataset/load_blender.py#L67C4-L114


With the main goal being to eliminate mis-shaping errors that may happen between training and testing elements of our dataset and to apply the makss provided. 

To run this code and obtain our results, you must include the following directory from the google drive linked: InfoNeRF Datasets/nerf_synthetic 

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

### More Datasets
To play with other scenes presented in the paper, download the data [here](https://drive.google.com/drive/folders/128yBriW1IG_3NJ5Rp7APSTZsJqdJdfc1). Place the downloaded dataset according to the following directory structure:
```
├── configs  
│   ├── ...    
│                                                                                      
├── data 
|   ├── nerf_synthetic
|   |   └── lego
|   |   └── ship    # downloaded synthetic dataset
|   |   └── ...
│   ├── DTU
│   │   └── scan1   # downloaded DTU dataset
│   │   └── scan2   # downloaded DTU dataset
|   |   └── ...
```

## Citation

If you find our work useful in your research, please cite:

```
@inproceedings{kim2022infonerf,
            author = {Mijeong Kim and Seonguk Seo and Bohyung Han},
            booktitle = {CVPR},
            title = {InfoNeRF: Ray Entropy Minimization for Few-Shot Neural Volume Rendering},
            year = {2022}
        }
```

## Acknowlegements

This code heavily borrows from [nerf-pytorch](https://github.com/yenchenlin/nerf-pytorch) and [DS-NeRF](https://github.com/dunbar12138/DSNeRF).
