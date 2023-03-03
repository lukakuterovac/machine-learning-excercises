import numpy as np
from PIL import Image, ImageEnhance

img = Image.open("road.jpg")

# a)
enhancer = ImageEnhance.Brightness(img)
enhancer.enhance(2).show("Brightness 1.5")

arr = np.asarray(img)
# b)
# Array COLSxROWS
parts = np.hsplit(arr, 4)
Image.fromarray(parts[1]).show()

# c)
rotate_img = np.rot90(arr, 3)
Image.fromarray(rotate_img).show()

# d)
flip_img = np.fliplr(arr)
Image.fromarray(flip_img).show()
