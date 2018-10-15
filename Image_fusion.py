import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt

path = 'C:\Research\Image_registrtion\Camera_Uploads'
os.chdir(path)
img = cv.imread('o1.jpg',0)
# Initiate ORB detector
orb = cv.ORB_create()
# find the keypoints with ORB
kp = orb.detect(img,None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# draw only keypoints location,not size and orientation
img2 = cv.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
plt.imshow(img2), plt.show()
                                        
