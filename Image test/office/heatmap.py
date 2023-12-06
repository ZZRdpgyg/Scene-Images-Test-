# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:42:17 2023

@author: ziruiz
"""

import csv
import matplotlib.pyplot as plt 
from pandas import *
import numpy as np

path = 'C:/Users/ziruiz/Desktop/image test/office/'
f = open(path + 'office_score.txt','r')
c = open(path + 'office_name.txt','r')
data = read_csv(path + 'office_score.txt') 
daname = read_csv(path + 'office_name.txt') 
sscore = data['office'].tolist()
name = daname['name'].tolist()

test_score = []
for i in sscore:
    if i != 1.0:
        test_score.append(i)

atscore = np.array(test_score)
print('max', np.max(atscore))
print('med',np.median(atscore))
print('mean', np.mean(atscore))
print('min', np.min(atscore))


hdata = np.array(sscore)
heat_data = np.reshape(hdata, (len(name),len(name)) # make the arrary of similarity results n x n array

np.savetxt(path + 'office_similarity_array.csv',heat_data,delimiter=',')
fig, ax = plt.subplots()

im = ax.imshow(heat_data)
ax.set_xticks(np.arange(len(name)), labels=name)
ax.set_yticks(np.arange(len(name)), labels=name)
plt.setp(ax.get_xticklabels(), rotation=90, ha="right",
         rotation_mode="anchor") #colour bar for the heatmap
cbar = ax.figure.colorbar(im, ax=ax, shrink=0.80) #colour bar for the heatmap
cbar.ax.set_ylabel('similarity', rotation=-90, va="bottom", fontsize = 70)
ax.set_title('Office Similarity', fontsize = 70)
fig.set_size_inches(25, 25, forward=True) # you can chenge your figure size here
fig.savefig('Office_similarity.jpg', dpi=300) #save as .jpg file
plt.show()