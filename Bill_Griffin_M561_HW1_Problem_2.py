# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 18:29:20 2019

@author: Bill Griffin

------------------------- Homework 1 / Problem  2
"""

path = r'C:\Users\Bill Griffin\Documents\Fall 2019\M561\Homework 1\Problem 2\itcont17to18.txt'

         # initialize
           
indivDict = {}
newAvg = oldAvg = newCount = oldCount = newSum = oldSum = 0

        # execute
        
with open(path) as file:
    for record in file:
        data = record.split('|') 
        contribution = int(data[14])
        donorName = data[7]
        try:
            oldSum, oldCount, oldAvg = indivDict[donorName]
            newCount = oldCount + 1
            newAvg = ((oldAvg * oldCount) + contribution) / newCount
            newSum = oldSum + contribution
            indivDict[donorName] = [newSum,newCount,newAvg]
        except:
            newAvg = contribution
            indivDict[donorName] = [contribution,1, newAvg]
         
s=[] 
for item in indivDict.keys():
    avg = indivDict[item][2]
    s1 = (item,avg)   
    try:
        s.append(s1)
    except:
        break

sorted_list = sorted(s,key = lambda x : x[1], reverse = True)    
for i in range(10):
    print(sorted_list[i])    
     

# -----------> OUTPUT

'''
('ENVIRONMENT AMERICA, INC.', 5895000.0)
('FREEDOM PARTNERS ACTION FUND', 5000000)
('ONE NATION', 4183333.3333333335)
('BEZOS, JEFF', 3378190.0)
('HOFFMAN, REID G.', 3053000)
('NATIONAL EDUCATION, ASSOCIATION', 3000000.0)
('CHARLES G. KOCH 1997 TRUST', 3000000)
('ACTION NOW INITIATIVE', 2469500.0)
('STEYER, THOMAS F.', 2281169.125)
('BLOOMBERG, MICHAEL R.', 2238179.0789473685)
'''           
