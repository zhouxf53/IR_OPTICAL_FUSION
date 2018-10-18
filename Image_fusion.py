import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

# regulate the path
path = 'C:\Research\Image_registrtion\Optical_images'
os.chdir(path)

# read both files
img1 = cv2.imread('o2.jpg',0)          # queryImage
img1 = cv2.resize(img1, (0,0), fx=0.20, fy=0.20) 
img2 = cv2.imread('i1.tif',0) # trainImage
img2 = np.fliplr(np.flipud(img2))
img2 = cv2.resize(img2, (0,0), fx=2, fy=2) 
# draw the boundary line for img1-visible image
edge1 = cv2.Canny(img1,100,200)
lines = cv2.HoughLines(edge1,1,np.pi/180,200)
slope1 = []
for line in lines:
    for rho,theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img1,(x1,y1),(x2,y2),(0,0,255),100)
        if x1 == x2:
            slope1.append(float('Inf'))
        else:
            slope1.append((y2-y1)/(x2-x1))



# draw the boudary line for img2-infrared image

##edge2 = cv2.Canny(img2,100,200)
##minLineLength = 2
##maxLineGap = 5
##lines = cv2.HoughLinesP(edge2,1,np.pi/180,100,minLineLength,maxLineGap)
##slope2 = []
##for line in lines:
##    for x1,y1,x2,y2 in line:
##        cv2.line(img2,(x1,y1),(x2,y2),(0,255,0),2)
##        if x1 == x2:
##            slope2.append(float('Inf'))
##        else:
##            slope2.append((y2-y1)/(x2-x1))
##plt.imshow(img2)
##plt.show()

                                
