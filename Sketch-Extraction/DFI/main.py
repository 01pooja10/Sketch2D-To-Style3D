import os 
import argparse
from dataset.dataset import get_loader
from solver import Solver
from PIL import Image 
import numpy as np 
from skimage.filters import gaussian
from numpy.fft import fft2, ifft2 
from pypher.pypher import psf2otf 

def main(config):
    test_loader = get_loader(test_mode=config.test_mode, sal_mode=config.sal_mode)
    if not os.path.exists(config.test_fold): os.mkdir(config.test_fold)
    test = Solver(test_loader, config)
    test.test(test_mode=config.test_mode)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Hyper-parameters
    parser.add_argument('--cuda', type=bool, default=True)

    # Testing settings
    parser.add_argument('--model', type=str, default='pretrained/dfi.pth')
    parser.add_argument('--test_fold', type=str, default='demo/predictions')
    parser.add_argument('--test_mode', type=int, default=3) # choose task
    parser.add_argument('--sal_mode', type=str, default='e') # choose dataset, details in 'dataset/dataset.py'

    config = parser.parse_args()
    main(config)

    #########################################################
    #       Load edge and saliency images and multiply      #
    #########################################################

    for i in range(100):
        predictions_dir = config.test_fold 
        img_name = f'r_{i}' 
        edge_img_name = img_name + '_edge.png' 
        sal_img_name = img_name + '_sal.png'
        edge_img_dir = os.path.join(predictions_dir, edge_img_name)
        sal_img_dir = os.path.join(predictions_dir, sal_img_name)

        # Define blur function 
        def fspecial_gaussian_2d(size, sigma):
            kernel = np.zeros(tuple(size))
            kernel[size[0]//2, size[1]//2] = 1
            kernel = gaussian(kernel, sigma)
            return kernel/np.sum(kernel)
        
        blur = lambda x, sigma: np.clip(np.real(ifft2(fft2(x) * psf2otf(fspecial_gaussian_2d((3, 3), sigma), (x.shape[0], x.shape[1])))), 0.0, 1.0)

        # Load images 
        img_edge = Image.open(edge_img_dir) 
        img_sal = Image.open(sal_img_dir) 

        # Compute salient edge image 
        img_edge = np.array(img_edge)
        img_sal = np.array(img_sal)
        img_sal = blur(img_sal, 1)
        img_edge_sal = img_edge * img_sal + 255 * np.ones_like(img_edge) * (1 - img_sal)
        img_edge_sal = np.clip(img_edge_sal * 15, 0.0, 255.0).astype(np.uint8) # Remove weaker background details 

        # Convert back to image 
        img_edge_sal = Image.fromarray(img_edge_sal).convert('RGB')

        # Save folder 
        folder_name = 'sketches'
        save_folder = os.path.join(predictions_dir,folder_name)
        if not os.path.exists(save_folder): os.mkdir(save_folder) 

        # Save image 
        img_edge_sal_name = img_name + '.png' 
        save_path = os.path.join(save_folder, img_edge_sal_name)
        img_edge_sal.save(save_path)
