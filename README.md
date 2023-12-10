# From Pencil Lines to 3D realms: Sketch Stylization with NeRF

We explore 2 unique approaches to generate and stylize a 3D object from a 2D set of sketches. To our knowledge, no prior work has been done on directly stylizing 3D models generated from sketches using neural radiance fields (NeRF).
1. We have stylization before rendering images from NeRF wherein we obtain the sketches, pass them through the neural style transfer model (MSG-Net), mask out the background, and then train NeRF on these stylized images. Here stylization is pixel-consistent and the results are in the style of the painting given. 
We also test a few-shot model called Info-NeRF with 4 and 10 images to test the ability of NeRF to reproduce reliable results with fewer volumes of input data.
![CI_imgs (2)](https://github.com/01pooja10/Sketch2D-To-Style3D/assets/66198904/602c0a0d-9b58-42a7-a714-9583d5f6af0b)

2. The second approach deals with stylization using text prompts while outputs are rendered by CLIP-NeRF. Here, we use transfer learning to substitute the NeRF in CLIP-NeRF with our model trained on the pencil sketches. This specifies a single color/textual information in the prompt rather than conditioning on a style image/painting.
<img width="840" alt="Screenshot 2023-12-09 at 7 39 21 PM" src="https://github.com/01pooja10/Sketch2D-To-Style3D/assets/30786246/61b3af2d-0fdb-4b35-b37e-39df68983665">

## Link to download data
The drive link to download different datasets and pretrained models is available here: https://drive.google.com/drive/folders/1mT1Hh4cCeEca2rt1IW_Ug241jBbsKGEd?usp=share_link




## Results

### Approach 1

Style Image 1:

![style1](https://github.com/01pooja10/Sketch2D-To-Style3D/assets/66198904/9fad3aeb-1f19-49a1-8637-3d98d1162911)

Training set of images consisting of sketches conditioned on Style 1 (painting):


https://github.com/01pooja10/Sketch2D-To-Style3D/assets/66198904/4ee69528-b95b-44d8-a56c-feee057df335



Style Image 2:

![style2](https://github.com/01pooja10/Sketch2D-To-Style3D/assets/66198904/ace1e20a-a768-4319-9e44-d798c34d1c7a)

Training set of images consisting of sketches conditioned on Style 2 (painting):


https://github.com/01pooja10/Sketch2D-To-Style3D/assets/66198904/46479018-1bea-4467-a484-fbd530857c97


#### InfoNeRF: 

4-shot with detailed sketch: 

![style_masked_fewshot_4](https://github.com/01pooja10/Sketch2D-To-Style3D/assets/110578288/a8249d09-1bf4-4308-bcdc-74aaf0b77e88)

10-shot with detailed sketch: 

![style_masked_fewshot_10](https://github.com/01pooja10/Sketch2D-To-Style3D/assets/110578288/26fad460-d0d0-44ee-b4a5-6bea807bb324)

4-shot with sparse sketch: 

![sparse_style_masked_fewshot_4](https://github.com/01pooja10/Sketch2D-To-Style3D/assets/110578288/355b6d00-64a1-470f-b657-3fcb9cdffc1a)

10-shot with sparse sketch: 

![sparse_style_masked_fewshot_10](https://github.com/01pooja10/Sketch2D-To-Style3D/assets/110578288/c6a23c6d-0c7f-440f-98e2-07871525f627)






