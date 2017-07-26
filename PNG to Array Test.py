import numpy as np
from PIL import Image

img = Image.open('C:\Users\Blake\PycharmProjects\AI-Research\White, '
                      'Black, '
               'White, Red, Green, Blue, Black, White, Black.png')
arr = np.array(img)

# record the original shape
shape = arr.shape
print shape
print arr
# make a 1-dimensional view of arr
flat_arr = arr.ravel()
print flat_arr
print flat_arr.size
# convert it to a matrix
vector = np.matrix(flat_arr)