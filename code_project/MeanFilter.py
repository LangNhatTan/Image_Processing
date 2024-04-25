import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt
import scipy.ndimage as sn
def MeanFilter(url):
    original = iio.imread(url)
    img = iio.imread(url,as_gray=True)
    # Create the filter with size 5x5
    filters = np.ones((5,5))/25
    # Performing convolution
    newImg = sn.convolve(img,filters).astype(np.uint8)
    fig = plt.figure(figsize=(10,7))
    fig.add_subplot(2,2,1)
    plt.imshow(original)
    plt.axis("off")
    plt.title("Original Image")
    fig.add_subplot(2,2,2)
    plt.imshow(newImg)
    plt.axis("off")
    plt.title("Image after use Mean filter")
    try:
        iio.imsave("New_img_LowPass.jpg",newImg)
    except:
        iio.imsave("New_img_LowPass.png",newImg)
    plt.show()
#MeanFilter("balloons_noisy.png")