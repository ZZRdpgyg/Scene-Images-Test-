# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:36:54 2023

@author: ziruiz
"""
import glob
import os

path = './'
num = 1
for i in glob.glob('*.png'):
    os.rename(i,'{}_office.png'.format(num))
    num+=1
    
