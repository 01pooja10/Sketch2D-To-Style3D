Adapted from the following repository: https://github.com/backseason/DFI 

Modifications performed to the following files: 
1. main.py - Added code after the following line to integrate salient mask and edge map into a sketch like representation of the original images:
https://github.com/01pooja10/Sketch2D-To-Style3D/blob/508a627ee4bbc7a2e4eb6da01628f480de4f7300/Sketch-Extraction/DFI/main.py#L32C5 

Ensure following directory structure exists: 
- demo/images
- demo/predictions
  - demo/predictions/sketches

where the original images to be converted must be in the demo/images directory, and the name of the image files to be read must be written in the demo/img.lst file. 

The final results (i.e. sketches extracted from original images) should be left in the demo/predictions/sketches directory. 

### Run (demo)
The source images are in the `demo/images` folder.
By running 
```shell
python main.py
```
you'll get the predictions under
the `demo/predictions` folder. The predictions of all the three tasks are performed simultaneously.

### Reference
```latex
@article{liu2020dynamic,
  title={Dynamic Feature Integration for Simultaneous Detection of Salient Object, Edge and Skeleton},
  author={Jiang-Jiang Liu and Qibin Hou and Ming-Ming Cheng},
  journal={IEEE Transactions on Image Processing},
  year={2020},
  volume={},
  number={},
  pages={1-15},
  doi={10.1109/TIP.2020.3017352},
}
```
