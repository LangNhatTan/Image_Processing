import imageio.v2 as iio
import matplotlib.pylab as plt
import numpy as np
def LogTransformation(url):
    originalImg = iio.imread(url)
    # show image
    fig = plt.figure(figsize=(10,10))
    fig.add_subplot(2,2,1)
    plt.imshow(originalImg)
    plt.axis('off')
    plt.title("Original Image")
    # Performing algorithm Log Transformation
    img = iio.imread(url,as_gray=True)
    matrixPixels = np.asarray(img)
    matrixFloatPixels = matrixPixels.astype(float)
    maxValue = matrixFloatPixels.max()
    logTransformation = (240.0 * np.log(1 + matrixFloatPixels)) / np.log(1 + maxValue)
    matrixInt = logTransformation.astype(np.uint8)
    # show image
    try:
        iio.imsave("New_img_LogTransformation.jpg",matrixInt)
    except:
        iio.imsave("New_img_LogTransformation.png",matrixInt)
    fig.add_subplot(2,2,2)
    plt.imshow(matrixInt)
    plt.axis("off")
    plt.title("Image after using Log Transformation")
    plt.show()
#LogTransformation("bird.png")