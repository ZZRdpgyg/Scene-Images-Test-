# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 22:29:05 2023

@author: Zirui Zhang
"""

import glob
import os
import cv2
import numpy as np
import csv
path = './'
f = ['{}_office.png'.format(i) for i in range(1,5)]

for i in f:
    first = cv2.imread(path + i)
    gray = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(i,gray)
        
        
        