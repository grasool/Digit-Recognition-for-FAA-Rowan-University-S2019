# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:21:52 2019

@author: Marc
"""

import cv2
import numpy as np

index = 0
subindex = 3

lower = np.array([228,228,228])
upper = np.array([255,255,255])

kernel = np.ones((1,1), np.uint8)
kernel2 = np.ones((2,2), np.uint8)
kernel3 = np.ones((3,3), np.uint8)
kernel4 = np.ones((4,4), np.uint8)

mask = cv2.imread('mask.jpg', 0)
mask2 = cv2.imread('mask2.jpg', 0)
corner = cv2.imread('corner.jpg', 0)
sev = cv2.imread('sevMask.jpg',0)

while index < 1000:
    
    im = cv2.imread('bigdata/'+ str(index) + '.jpg',0)
    
    corn = cv2.bitwise_or(im, corner)
    
    erosion = cv2.erode(im, kernel, iterations = 1)
      
    #thresh2 = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    ret, thresh = cv2.threshold(corn, 128,255,cv2.THRESH_TOZERO)
    
    masked = cv2.bitwise_and(thresh, mask)
    ret, thresh2 = cv2.threshold(masked, 128,255,cv2.THRESH_BINARY)
    
    # thresh2 is perfect block. do not edit
    
    blur = cv2.blur(thresh2,(5,5),0)
    erode = cv2.erode(blur, kernel3, iterations = 1)
    ret, thresh3 = cv2.threshold(erode, 128,255,cv2.THRESH_TOZERO)
    sevm = cv2.bitwise_or(thresh3, sev)
    morph = cv2.morphologyEx(sevm, cv2.MORPH_OPEN, kernel2)
    
    proper = sevm
    cv2.imwrite('bigdataFilt/'+ str(index) +'.jpg', proper)   
    index = index +1