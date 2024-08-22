# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:32:38 2023

@author: ziruiz
"""
import cv2
import numpy as np

image = cv2.imread('3_office.png', 0 )

tem_list = ['3_office_cropped_image2.jpg']
clone = image.copy()
for i in tem_list:
    
    template = cv2.imread(i,0)
    (tW, tH) = template.shape[::-1]
    
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    #print(result)
    
    threshold = 0.95
    (yCoords, xCoords) = np.where(result >= threshold)
    
    #print(yCoords, xCoords)
    
    
    for (x, y) in zip(xCoords, yCoords):
        # draw the bounding box on the image
        cv2.rectangle(clone, (x, y), (x + tW, y + tH), 1)
        # show our output image *before* applying non-maxima suppression
    #cv2.imshow("Before NMS", clone)
    #cv2.waitKey(0)
cv2.imwrite('output match.jpg', clone)
