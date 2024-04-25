import imageio.v2 as iio
import matplotlib.pylab as plt
import numpy as np
def LowPassFilter(url,value):
    org = iio.imread(url)
    f = iio.imread(url,as_gray=True)
    fig = plt.figure(figsize=(8,8))
    fig.add_subplot(2,2,1)
    plt.imshow(org)
    plt.axis("off")
    plt.title("Original image")
    # image in frequency domain
    F = np.fft.fft2(f)
    Fshift = np.fft.fftshift(F)

    # Filter: Low pass filter
    M,N = f.shape[0],f.shape[1]
    H = np.zeros((M,N), dtype=np.float32)
    D0 = value
    for u in range(M):
        for v in range(N):
            D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
            if D <= D0:
                H[u,v] = 1
            else:
                H[u,v] = 0

    # Ideal Low Pass Filtering
    Gshift = Fshift * H
    # Inverse Fourier Transform
    G = np.fft.ifftshift(Gshift)

    g = np.abs(np.fft.ifft2(G))
    try:
        iio.imsave("New_img_LowPass.jpg",g)
    except:
        iio.imsave("New_img_LowPass.png",g)
    fig.add_subplot(2,2,2)
    plt.imshow(g, cmap='gray')
    plt.axis('off')
    plt.title(f"Image after using Low pass filter with D0 = {value}")
    plt.show()
LowPassFilter("balloons_noisy.png", 200)