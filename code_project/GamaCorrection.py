import imageio.v2 as iio
import matplotlib.pylab as plt
import numpy as np
def GammaCorrection(url, gammaHigh):
    original_img = iio.imread(url)
    # show original image
    fig = plt.figure(figsize=(10,8))
    fig.add_subplot(2,2,1)
    plt.imshow(original_img)
    plt.axis("off")
    plt.title("Original Image")
    # Using gamma to enhance the image
    img = iio.imread(url)
    invgammaHigh = 1/gammaHigh
    matrixPixels = np.asarray(img)
    matrixFloat = matrixPixels.astype(float)
    maxValue = matrixFloat.max()
    recipes = matrixFloat/maxValue
    computeLogHighGamma = np.log(recipes) * invgammaHigh
    computeExpHighGamma = np.exp(computeLogHighGamma) * 255.0
    matrixIntHigh = computeExpHighGamma.astype(np.uint8)
    # show image after adding gamma
    fig.add_subplot(2,2,2)
    plt.imshow(matrixIntHigh)
    plt.axis("off")
    plt.title(f"Image with gamma = {gammaHigh}")
    # fig.add_subplot(2,2,3)
    # plt.imshow(matrixIntLow)
    # plt.axis("off")
    # plt.title("Image with gamma = 0.5")
    plt.show()
#GammaCorrection("bird.png",4.4,0.5)
