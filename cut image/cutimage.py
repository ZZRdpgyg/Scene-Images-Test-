# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 12:10:38 2022

@author: ziruiz
"""

import cv2 
import numpy as np
import os





img = cv2.imread("./1_office.png")



rows, cols, _ = img.shape
    
print("Rows", rows)
print("cols", cols)
    
    #create a new folder to store your new images... my new folder name is 2, so update the new path
occluder = img[int(rows/2):int(rows), int(cols/2):int(cols)]
cv2.imwrite("./office_occ.png",occluder) 
    
    
    
    
    #pts = a.reshape((-1,1,2))
img[300:600, 400:800] = [255,255,255]
   
#[0:300, 0:400] = upper left
#[300:600, 400:800] = lower right
#..please seek other option.. 
    
cv2.imwrite("./office_con.png",img)
    
    
#img2 = cv2.imread(':/Users/ziruiz/Desktop/Image test/stimuli_org/cit_1_con.png')

#img2[0:300, 0:800] = [255,255,255]

#cv2.imwrite(':/Users/ziruiz/Desktop/Image test/stimuli_org/test2.png', img2) 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    