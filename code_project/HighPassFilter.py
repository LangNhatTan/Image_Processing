import matplotlib.pylab as plt
import imageio.v2 as iio
import numpy as np
def HighPassFilter(url,value):
    img = iio.imread(url,as_gray=True)
    fig = plt.figure(figsize=(8,8))
    fig.add_subplot(2,2,1)
    plt.imshow(img)
    plt.axis("off")
    plt.title("Original image")

    fft = np.fft.fft2(img)
    fftShift = np.fft.fftshift(fft)
    # Filter: High pass filter
    M,N = img.shape[0],img.shape[1]
    D0 = value
    H = np.zeros((M,N),dtype=np.float32)
    center1,center2 = M/2,N/2
    for i in range(M):
        for j in range(N):
            D = np.sqrt((i-center1)**2 + (j- center2)**2)
            if D <= D0:
                H[i,j] = 1
            else:
                H[i,j] = 0

    # Ideal High pass filter
    H = 1 - H
    Gshift = fftShift * H
    G = np.fft.ifftshift(Gshift)
    newImg = np.abs(np.fft.ifft2(G))
    fig.add_subplot(2,2,2)
    plt.imshow(newImg)
    plt.axis("off")
    plt.title(f"Image after using High pass filter with D0 = {value}")
    plt.show()