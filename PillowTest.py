from PIL import Image

def main():
    filename = 'lena_512x512.bmp'
    imageFromFile = Image.open(filename)
    imageBuffer = Image.new('RGB', imageFromFile.size)
    for y_pos in range(imageFromFile.size[1]):
        for x_pos in range(imageFromFile.size[0]):
            (inR, inG, inB) = imageFromFile.getpixel((x_pos, y_pos))
            Y = int(inR * .3 +  inG * .6 + inB*.1)
            outR = Y
            outG = Y
            outB = Y
            imageBuffer.putpixel((x_pos, y_pos), (outR, outG, outB))
    imageBuffer.show()

if __name__ == "__main__":
    main()