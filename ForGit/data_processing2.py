# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:46:37 2019

@author: Marc
"""

import cv2
import numpy as np

index = 0
subindex = 3

lower = np.array([220,220,220])
upper = np.array([255,255,255])

while index < 1000:
    
    im = cv2.imread('unscaled_data/'+str(index)+'_3.jpg')
    blank = cv2.imread('28x28.jpg')
    scaled = cv2.resize(im, None,  fx = 4, fy = 4, interpolation = cv2.INTER_NEAREST)
    #inverted = cv2.bitwise_not(scaled)
    rightSize = cv2.copyMakeBorder(scaled, 0,0,4,4, cv2.BORDER_CONSTANT, value = [0,0,0])
    
    bigboy = cv2.resize(rightSize, None, fx = 8, fy = 8, interpolation = cv2.INTER_CUBIC)
    
    #hsv = cv2.cvtColor(rightSize, cv2.COLOR_BGR2HSV)
    filtered = cv2.inRange(rightSize, lower, upper)
    cv2.imwrite('new-Filtered/' + str(index) +'.jpg', rightSize)

    
    index = index + 1