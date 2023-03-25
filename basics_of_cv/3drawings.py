import cv2
import numpy as np

# Made a window with single color channel
blank_img_with_one_channel = np.zeros((350,350),dtype=np.uint8)

# The cv2.line() function takes these parameters as follows
# cv2.line(input the matrix frame, startingpoint, endingpoint, color, thickness)
cv2.line(blank_img_with_one_channel,(0,0),(350,350),(255),3)
cv2.imshow('grey frame', blank_img_with_one_channel)

'''So the reason to have 2 windows poped up is to show that what color channels are so these
are nothing but the BGR colors refered as channels so when we make a matrix size of 350,350 we are
making a single colored channel that is from dark=>0 to light=>255 so while choosing colors i used 
255 which is light, In the next one it has three channels which means we can see colors so the 4rth
parameter is the color which takes a tuple of (B,G,R) so that ranges from 0-255 so i choose green to dsiplay'''

blank_img_with_three_channel = np.zeros((350,350,3),dtype=np.uint8)
cv2.line(blank_img_with_three_channel,(0,0),(350,350),(0,255,0),3)
cv2.imshow('color frame', blank_img_with_three_channel)


cv2.waitKey(0)