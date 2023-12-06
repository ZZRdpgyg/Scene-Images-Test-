# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 09:58:03 2023

@author: Zirui Zhang
"""
import glob
import os
import skimage
import cv2
import numpy as np
import csv






#f = ['1_office.png', '3_office.png']
f = ['21_city.png', '49_city.png']
first = cv2.imread(f[1])
second = cv2.imread(f[0])
        
        # Convert images to grayscale
first_gray = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
second_gray = cv2.cvtColor(second, cv2.COLOR_BGR2GRAY)
        
        # Compute SSIM between two images
score, diff = skimage.metrics.structural_similarity(first_gray, second_gray, full=True)


        
        

        
        





 
# # The diff image contains the actual image differences between the two images
# # and is represented as a floating point data type so we must convert the array 
# # to 8-bit unsigned integers in the range [0,255] before we can use it with OpenCV
diff = (diff * 255).astype("uint8")
# 
# # Threshold the difference image, followed by finding contours to
# # obtain the regions that differ between the two images
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
# 
# # Highlight differences
mask = np.zeros(first.shape, dtype='uint8')
filled = second.copy()
# 
for c in contours:
    area = cv2.contourArea(c)
    if area > 100:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(first, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.rectangle(second, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.drawContours(mask, [c], 0, (0,255,0), -1)        
        cv2.drawContours(filled, [c], 0, (0,255,0), -1)
 
# =============================================================================
# cv2.imshow('first', first)
# cv2.imwrite('office_first.png',first)
# cv2.imshow('second', second)
# cv2.imwrite('office_second.png',second)
# cv2.imshow('diff', diff)
# cv2.imwrite('office_diff.png',diff)
# cv2.imshow('mask', mask)
# cv2.imwrite('office_mask.png',mask)
# cv2.imshow('filled', filled)
# cv2.imwrite('office_filled.png',filled)
# cv2.waitKey()
# 
# =============================================================================

cv2.imshow('first', first)
cv2.imwrite('ce_first.png',first)
cv2.imshow('second', second)
cv2.imwrite('ce_second.png',second)
cv2.imshow('diff', diff)
cv2.imwrite('ce_diff.png',diff)
cv2.imshow('mask', mask)
cv2.imwrite('ce_mask.png',mask)
cv2.imshow('filled', filled)
cv2.imwrite('ce_filled.png',filled)
cv2.waitKey()
# =============================================================================
