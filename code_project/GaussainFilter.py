from PIL import Image, ImageFilter
import imageio.v2 as iio
import matplotlib.pylab as plt
def GaussianFilter(url):
    img1 = Image.open(url).convert("L")
    fig = plt.figure(figsize=(8,8))
    fig.add_subplot(2,2,1)
    plt.imshow(img1)
    plt.axis("off")
    plt.title("Original image")
    img2 = img1.filter(ImageFilter.GaussianBlur)
    try:
        iio.imsave("New_img_Gaussian.jpg",img2)
    except:
        iio.imsave("New_img_Gaussian.png",img2)
    fig.add_subplot(2,2,2)
    plt.imshow(img2)
    plt.axis("off")
    plt.title("ImageFilter")
    plt.show()
#GaussianFilter()