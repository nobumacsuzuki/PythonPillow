from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2

def PillowPractice1():
    filename = 'lena_512x512.bmp'
    imageFromFile = Image.open(filename) # it generates the PIL.Image.Image object

    # use OpenCV as viewer
    ndarrayImageColorRGB = np.array(imageFromFile) # if np.asarray, the array become immutable (cannot edit)
    print(ndarrayImageColorRGB)
    print(ndarrayImageColorRGB.dtype)
    print(ndarrayImageColorRGB.shape)
    ndarrayImageColorBGR = cv2.cvtColor(ndarrayImageColorRGB, cv2.COLOR_BGR2RGB) # convert RGB to BGR, cv2 takes BGR array
    cv2.imshow('Color image RGB as BGR', ndarrayImageColorRGB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow('Color image after BGR2RGB', ndarrayImageColorBGR)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    # mask green and blue
    #ndarrayImageColorRGB[:, :, 0] = 0
    ndarrayImageColorRGB[:, :, 1] = 0
    ndarrayImageColorRGB[:, :, 2] = 0

    ndarrayImageColorBGR = cv2.cvtColor(ndarrayImageColorRGB, cv2.COLOR_BGR2RGB) # convert BGR to RGB
    cv2.imshow('Color image', ndarrayImageColorBGR)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # manipulate R, G, B to set all to Y
    imageBuffer = Image.new('RGB', imageFromFile.size) # it generates the PIL.Image.Image object
    for y_pos in range(imageFromFile.size[1]):
        for x_pos in range(imageFromFile.size[0]):
            (inR, inG, inB) = imageFromFile.getpixel((x_pos, y_pos)) # the cordinate is type, it returns pixel value of tuple
            Y = int(inR * .3 +  inG * .6 + inB * .1)
            outR = Y
            outG = Y
            outB = Y
            imageBuffer.putpixel((x_pos, y_pos), (outR, outG, outB)) # the cordinate is type, the pixel value is tuple

    # use OpenCV as viewer
    ndarrayImageYonly = np.array(imageBuffer)
    print(ndarrayImageYonly)
    print(ndarrayImageYonly.dtype)
    print(ndarrayImageYonly.shape)
    cv2.imshow('Y channel only',ndarrayImageYonly)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    PillowPractice1()

if __name__ == "__main__":
    main()