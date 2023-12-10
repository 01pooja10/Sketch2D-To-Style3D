# From Pencil Lines to 3D realms: Sketch Stylization with NeRF

We explore 2 unique approaches to generate and stylize a 3D object from a 2D set of sketches. To our knowledge, no prior work has been done on directly stylizing 3D models generated from sketches using neural radiance fields (NeRF).
1. We have stylization before rendering images from NeRF wherein we obtain the sketches, pass them through the neural style transfer model (MSG-Net), mask out the background, and then train NeRF on these stylized images. Here stylization is pixel-consistent and the results are in the style of the painting given. 
We also test a few-shot model called Info-NeRF with 4 and 10 images to test the ability of NeRF to reproduce reliable results with fewer volumes of input data.
![CI_imgs (2)](https://github.com/01pooja10/Sketch2D-To-Style3D/assets/66198904/602c0a0d-9b58-42a7-a714-9583d5f6af0b)

2. The second approach deals with stylization using text prompts while outputs are rendered by CLIP-NeRF. Here, we use transfer learning to substitute the NeRF in CLIP-NeRF with our model trained on the pencil sketches. This specifies a single color/textual information in the prompt rather than conditioning on a style image/painting.
<img width="840" alt="Screenshot 2023-12-09 at 7 39 21 PM" src="https://github.com/01pooja10/Sketch2D-To-Style3D/assets/30786246/61b3af2d-0fdb-4b35-b37e-39df68983665">

# Results

## Approach 1
Style Image 1:
![style1](https://github.com/01pooja10/Sketch2D-To-Style3D/assets/66198904/9fad3aeb-1f19-49a1-8637-3d98d1162911)
Training set of images consisting of sketches conditioned on Style 1 (painting):
https://github.com/01pooja10/Sketch2D-To-Style3D/assets/66198904/b7b72e53-a12f-4af3-a136-d4a4ca8ccd7e

Style Image 2:
![style2](https://github.com/01pooja10/Sketch2D-To-Style3D/assets/66198904/ace1e20a-a768-4319-9e44-d798c34d1c7a)

Training set of images consisting of sketches conditioned on Style 2 (painting):
https://github.com/01pooja10/Sketch2D-To-Style3D/assets/66198904/d2d1f4b0-69b5-4da3-afae-9ceae5ce2b4f





