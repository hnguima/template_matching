
from PIL import Image
import matplotlib.pyplot as plt

import numpy as np

import sys
import time

image_jpg = Image.open(sys.argv[1])
image_bw = image_jpg.convert("L")

template_jpg = Image.open(sys.argv[2])
template_bw = template_jpg.convert("L")

image = np.array(image_bw)
template = np.array(template_bw)

template_rows, template_cols = template.shape
image_rows, image_cols = image.shape

match_arr = np.zeros((image_rows - template_rows,image_cols - template_cols))
    
# plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)

imgplot = ax.imshow(image)

delay = 0

for i in range(0, image_rows - template_rows, 1):
  for j in range(0, image_cols - template_cols, 1):

    match_img = np.absolute(image[i:i + template_rows,j:j + template_cols] - template)
    match_arr[i, j] = np.sum(match_img)


    # delay = (delay + 1) % 2000

    # if delay == 0:
    #   new_image = np.copy(image);
    #   new_image[i:i + template_rows, j:j + template_cols] = match_img;
    #   imgplot.set_data(new_image)
    #   fig.canvas.draw()
    #   fig.canvas.flush_events()

    # time.sleep(0.1)


min_row, min_col = np.where(match_arr == match_arr.min())

print(min_row[0])
print(min_col[0])
print(match_arr.min())

print(np.absolute(image[min_row[0]:min_row[0] + template_rows,min_col[0]:min_col[0] + template_cols] - template))

match_img = image[min_row[0]:min_row[0] + template_rows,min_col[0]:min_col[0] + template_cols] - template
match_img = Image.fromarray(np.uint8(match_img))
match_img.show()

image_color = np.array(image_jpg)

new_image = np.copy(image_color);

new_image[min_row[0]:min_row[0] + template_rows, min_col[0] - 2 : min_col[0] + 2] = [255, 0, 0]
new_image[min_row[0]:min_row[0] + template_rows, (min_col[0] + template_cols) - 2 :(min_col[0] + template_cols) + 2] = [255, 0, 0]
new_image[min_row[0] - 2 : min_row[0] + 2, min_col[0]:min_col[0] + template_cols] = [255, 0, 0]
new_image[(min_row[0] + template_rows) - 2 : (min_row[0] + template_rows) + 2, min_col[0]:min_col[0] + template_cols] = [255, 0, 0]

out_jpg = Image.fromarray(np.uint8(new_image))
out_jpg.show()