import cv2
#import pandas as pd
#Crop and Save individual digits

index = 9999

while index < 10000:
    
    im = cv2.imread('Latitude(deg)/'+str(index)+'.jpg')

    #dig_1 = im[6:5, 10:15]
    #dig_2 = im[11:5, 15:15]
   # dig_3 = im[16:5, 20:15]
    
    dig_1 = im[5:12, 5:10]
    dig_2 = im[5:12, 10:15]
    dig_3 = im[5:12, 15:20]
    
    dig_1 = cv2.cvtColor(dig_1, cv2.COLOR_BGR2GRAY)
    dig_2 = cv2.cvtColor(dig_2, cv2.COLOR_BGR2GRAY)
    dig_3 = cv2.cvtColor(dig_3, cv2.COLOR_BGR2GRAY)
    
    cv2.imwrite('data/' + str(index) +'_1.jpg', dig_1)
    cv2.imwrite('data/' + str(index) +'_2.jpg', dig_2)
    cv2.imwrite('data/' + str(index) +'_3.jpg', dig_3)
    
    index = index + 1