from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2

def main():
    filename = 'lena_512x512.bmp'
    imageFromFile = Image.open(filename) # it generates the PIL.Image.Image object

    # use OpenCV as viewer
    cv2Image = np.asarray(imageFromFile)
    cv2Image = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2RGB)
    cv2.imshow('Color image', cv2Image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    imageBuffer = Image.new('RGB', imageFromFile.size) # it generates the PIL.Image.Image object
    for y_pos in range(imageFromFile.size[1]):
        for x_pos in range(imageFromFile.size[0]):
            (inR, inG, inB) = imageFromFile.getpixel((x_pos, y_pos)) # the cordinate is type, it returns pixel value of tuple
            Y = int(inR * .3 +  inG * .6 + inB*.1)
            outR = Y
            outG = Y
            outB = Y
            imageBuffer.putpixel((x_pos, y_pos), (outR, outG, outB)) # the cordinate is type, the pixel value is tuple

    # use OpenCV as viewer
    cv2Image = np.asarray(imageBuffer)
    cv2Image = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2RGB)
    cv2.imshow('Y channel only',cv2Image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    imageGray = imageFromFile.convert('L') # it convers 8 bit/pixel, grayscale, L = R * 299/1000 + G * 587/1000 + B * 114/1000
    arrayImageGray = np.asarray(imageGray)

    # FFT and centered
    arrayFFTed = np.fft.fft2(arrayImageGray)
    arrayShiftedFFTed = np.fft.fftshift(arrayFFTed)
    arrayPowerSpectrumFFTRealPart = 20 * np.log(np.absolute(arrayShiftedFFTed))
    # Uncentered and Inverse FFT
    arrayRevertedShiftedFFTed = np.fft.fftshift(arrayShiftedFFTed)
    arrayInvertFFTed = np.fft.ifft2(arrayRevertedShiftedFFTed).real


    # 上記を画像として可視化する
    fig, axes = plt.subplots(1, 3, figsize=(8, 4))
    # 枠線と目盛りを消す
    for ax in axes:
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])
    # 元画像
    axes[0].imshow(arrayImageGray, cmap='gray')
    axes[0].set_title('Input Image')
    # 周波数領域のパワースペクトル
    axes[1].imshow(arrayPowerSpectrumFFTRealPart, cmap='gray')
    axes[1].set_title('Magnitude Spectrum')
    # FFT -> IFFT した画像
    axes[2].imshow(arrayInvertFFTed, cmap='gray')
    axes[2].set_title('Reversed Image')
    # グラフを表示する
    plt.show()

if __name__ == "__main__":
    main()