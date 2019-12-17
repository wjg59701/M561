# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:49:24 2019

@author: Bill Griffin

---------------------------- Homework 3 ------------------------------

"""

import numpy as np
np.set_printoptions(precision = 2, floatmode = 'fixed')

fileName = r"C:\Users\Bill Griffin\Documents\Fall 2019\M561\Homework 3\kc_house_data.csv"

with open(fileName) as g:
    records = g.readlines()
variableNames= records[0].split(',')

n = len(records) - 1
k = np.matrix(np.zeros((n,5)))
   
for i, record in enumerate(records[1:]):    
    lst = record.split(',')
    for j in range(2,7):    
        k[i,j-2] = float(lst[j])
    
k = np.sort(k, axis = 0) 

j = np.matrix(np.ones((n,3)))

trim = [.005, .025, .05]

for q in range(3):          
    for r in range(int(trim[q] * n)):
        j[r, q] = 0
        j[((n - 1) - r), q] = 0 

rawM = np.matrix(np.zeros((6, 6)))  
xm = np.matrix(np.ones((6, 1)))
xbar = []

for x in range(n):
    xm[1:,0] = k[x,:].T
    rawM += xm @ xm.T
xbar = [rawM[0, 1:]/n]

print('Untrimmed Means are -> ', xbar)

trimmed_xbar = []
for m in range(3):    
    for n in range(5):
        a = (k[:,n].T @ j[:,m]) / (j[:,m].T @ j[:,m])
        a = float(a)        
        trimmed_xbar.append(a)        
    print('The ',trim[m]*100,'% trimmed means are -> ', trimmed_xbar )
    trimmed_xbar = []
    


# Output -->
    
'''

Untrimmed Means are ->  [matrix([[5.40e+05, 3.37e+00, 2.11e+00, 2.08e+03, 1.51e+04]])]
The  0.5 % trimmed means are ->  [528766.2805533486, 3.3642566714960043, 2.1062298453054167, 2064.3862691031454, 13094.133944010842]
The  2.5 % trimmed means are ->  [509254.5162421468, 3.3526031266741345, 2.0884551697267812, 2036.0802123411095, 10285.750986217308]
The  5.0 % trimmed means are ->  [495922.3374286742, 3.3444198838225465, 2.0792679792319952, 2013.8501516475608, 9236.48727702668]

'''
