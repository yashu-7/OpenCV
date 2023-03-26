import cv2
import numpy as np

blank_window = np.zeros((350,350,3),dtype=np.uint8)
# Rectangle
cv2.rectangle(blank_window, (100,100), (250,205), (0,0,255), 1)

# Circle
cv2.circle(blank_window, (175,175), 30, (255,0,0), -1)

# Text
cv2.putText(blank_window,'Hello', (0,25), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0), 1)

''' These are some examples to show different types of operations that can be done
    on a image/frames/array of matrix
'''
cv2.imshow('window', blank_window)
cv2.waitKey(0)