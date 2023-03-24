import cv2
# creating an object to capture the data from camera if you are using externam camera use
# 1 or 2 ... in place of 0
cam = cv2.VideoCapture(0)

# As video is continous frames we use while loop with always true condition or also called infinite loop
while 1:
    # cam.read() return a bool and the matrix values 
    ret, frame = cam.read()
    if not ret:
        print('unable to stream....')
        break
    
    # We are using the matrix returned to frame by cam.read() to display the image
    cv2.imshow('cam',frame)

    # This is to quqit out of the loop if you press q it quits out of the infinite loop
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()