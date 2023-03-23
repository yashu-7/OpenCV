import cv2
import numpy as np
blank_window = np.zeros((250,250),dtype=np.float32)
url = '//give the path to image'
# what cv.imread() does is it loads the image from file and returns a 2d or 3d matrix,
#  depending on the channels (channels means the colors BGR or gray for example)
img = cv2.imread(url)

# cv2.imshow() displays the image in a window taking window name and the image array as input
cv2.imshow('blank window',blank_window)
cv2.imshow('image',img)

# Now when we run it without cv2.waitKey() it kills the window right after it is displayed
# so we now use delay to display it '0' in this case means we are freezing it we can give the time after 
# it needs to shutdown remember the input is in 'ms'
cv2.waitKey(0)