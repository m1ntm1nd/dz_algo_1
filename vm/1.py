import cv2
import numpy as np

img = (np.random.random((300, 300, 3)) * 255.).astype(np.uint8)
# let's save 4 images (color/gray, png/jpg)
cv2.imwrite('img-png-gray.png', img[:, :, 1])  # output size: 90KB
