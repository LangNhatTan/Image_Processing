import imageio.v2 as iio
import scipy.ndimage as sn
import matplotlib.pylab as plt
import numpy as np
def MinimumAndMaximumFilter(url):
    originalImage = iio.imread(url)
    image = iio.imread(url,as_gray=True).astype(np.uint8)
    minimumFilter = sn.minimum_filter(image,size=2,footprint=None,output=None,mode="reflect",cval=0.0,origin=0)
    maximumFilter = sn.maximum_filter(image,size=2,footprint=None,output=None,mode="reflect",cval=0.0,origin=0)
    fig = plt.figure(figsize=(10,10))
    # show image original image
    fig.add_subplot(2,2,1)
    plt.imshow(originalImage)
    plt.axis("off")
    plt.title("Original Image")
    # Show image after using minimum filter
    fig.add_subplot(2,2,2)
    plt.imshow(minimumFilter)
    plt.axis("off")
    plt.title("Image after using minimum filter")
    # Show image after using maximum filter
    fig.add_subplot(2,2,3)
    plt.imshow(maximumFilter)
    plt.axis("off")
    plt.title("Image after using maximumfilter")
    
    plt.show()
#MinimumAndMaximumFilter("salt-pepper_noisy.png")