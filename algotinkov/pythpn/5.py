import cv2

# path
path = r'/home/fuse-power/Desktop/ITlab progress/Images/humanpose.jpg'
  
# Reading an image in default mode
src = cv2.imread(path)
  
# Window name in which image is displayed
window_name = 'Image'
  
# Using cv2.transpose() method
image = src.transpose((2, 0, 1))
  
# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)