from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2

def main():
    filename = 'lena_512x512.bmp'
    imageFromFile = Image.open(filename) # it generates the PIL.Image.Image object
    imageFromFile.show()
    input()


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
    imageBuffer.show()

if __name__ == "__main__":
    main()