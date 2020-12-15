from PIL import Image
import numpy as np

filename = 'lena_512x512.bmp'
imageFromFile = Image.open(filename)
imageArray = np.array(imageFromFile)
imageFromArray = Image.fromarray(imageArray)
print(imageArray)
imageFromArray.show()
