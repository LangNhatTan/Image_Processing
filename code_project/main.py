import GamaCorrection
import GaussainFilter
import LogTransformation
import LowPassFilter
import HighPassFilter
import Minimum_Maximum_Filter
import MedianFilter
import MeanFilter
print("Thuat toan khoi phuc anh")
print("1. Gamma Correction")
print("2. Gaussian Filter")
print("3. HighPass Filter")
print("4. LowPass Filter")
print("5. Mean Filter")
print("6. Median Filter")
print("7. Minimum_Maximum filter")
print("8. Log Transformation")
print("Nhan 9 de thoat chuong trinh","\n")

print("Anh can khoi phuc")
print("1. bird.png")
print("2. balloons_noisy.png")
print("3. gaussian_noise.jpg")
print("4. salt-pepper_noisy.png")
check = "r"
while check != "e":
    user = input("Nhap thuat toan so: ")
    if user == "9":
        check = "e"
        continue
    img = input("Nhap ten anh: ")
    if user == "1":
        gammaHigh = float(input("Nhap he so gamma: "))
        GamaCorrection.GammaCorrection(img,gammaHigh)
    elif user == "2":
        GaussainFilter.GaussianFilter(img)
    elif user == "3":
        value = int(input("Nhap gia tri D0 = "))
        HighPassFilter.HighPassFilter(img,value)
    elif user == "4":
        value = int(input("Nhap gia tri D0 = "))
        LowPassFilter.LowPassFilter(img,value)
    elif user == "5":
        MeanFilter.MeanFilter(img)
    elif user == "6":
        MedianFilter.MedianFilter(img)
    elif user == "7":
        Minimum_Maximum_Filter.MinimumAndMaximumFilter(img)
    elif user == "8":
        LogTransformation.LogTransformation(img)

