# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:22:42 2024

@author: ziruiz
"""

import cv2

# read the input image
image = cv2.imread('./3_office.png')

# define the alpha and beta
alpha = 1 # Contrast control
beta = 1 # Brightness control

# call convertScaleAbs function
adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# display the output image
cv2.imshow('adjusted', adjusted)
cv2.imwrite('3_office_adjust.png',adjusted)
