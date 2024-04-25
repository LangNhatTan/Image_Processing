import imageio.v2 as iio
import scipy.ndimage as sn
import matplotlib.pylab as plt
import numpy as np
def MedianFilter(url):
    originalImage = iio.imread(url)
    image = iio.imread(url,as_gray=True).astype(np.uint8)
    # Design size of the figure
    fig = plt.figure(figsize=(8,7))
    newImg = sn.median_filter(image,size=5,footprint=None,output=None,mode="reflect",cval=0.0,origin=0)
    fig.add_subplot(2,2,1)
    plt.imshow(originalImage)
    plt.axis("off")
    plt.title("Original Image")
    # show image after using median filter
    fig.add_subplot(2,2,2)
    plt.imshow(newImg)
    plt.axis("off")
    plt.title("Image after using Median Filter")
    try:
        iio.imsave("New_img_LowPass.jpg",newImg)
    except:
        iio.imsave("New_img_LowPass.png",newImg)
    plt.show()
#MedianFilter("balloons_noisy.png")