# Stylization
This folder contains all the code files and dependencies required for stylizing input images. This code has been adapted from https://github.com/zhanghang1989/PyTorch-Multi-Style-Transfer

The code for stylization is made available here. To use the MSG-Net pretrained model, follow the instructions given below.

The following modifications have been made: 
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/20aef0221049c4669aa921875d07c7c0f75c96f6/sketch-style-3d/stylization/experiments/main.py#L227
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/20aef0221049c4669aa921875d07c7c0f75c96f6/sketch-style-3d/stylization/experiments/main.py#L235
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/20aef0221049c4669aa921875d07c7c0f75c96f6/sketch-style-3d/stylization/experiments/main.py#L260

https://github.com/01pooja10/Sketch2D-To-Style3D/blob/0e888deb02f596c05a65d70b0aec7da45787ecb3/sketch-style-3d/stylization/experiments/option.py#L84
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/0e888deb02f596c05a65d70b0aec7da45787ecb3/sketch-style-3d/stylization/experiments/option.py#L84

## Run files
To use this folder for stylizing your own set of sketches (or other images), run the following line:
```
python main.py eval --content-folder /path/to/sketches/ --style-image /path/to/style/image --output-folder /path/to/outputs --model models/21styles.model --content-size 800 --style_size 800
```

## Results
In the figure below we display some outputs after stylization and masking out the colored background region to obtain a stylized foreground object with a plain white background.
![Output images](https://github.com/01pooja10/Sketch2D-To-Style3D/assets/66198904/d03566e3-aea9-42f8-930f-5eb1b17fdf6b)

## Citation
If you use this work, please cite the original paper and its authors:
```
@article{zhang2017multistyle,
	title={Multi-style Generative Network for Real-time Transfer},
	author={Zhang, Hang and Dana, Kristin},
	journal={arXiv preprint arXiv:1703.06953},
	year={2017}
}
```
