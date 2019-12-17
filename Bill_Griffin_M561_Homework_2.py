# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 08:06:54 2019

@author: Bill Griffin

--------------------------- Homework 2 - M561 ------------------------------

"""


path = r'C:\Users\Bill Griffin\Documents\Fall 2019\M561\Homework 2\Names.txt'


# Create babyDict with (year,sex) tuple as key and list of names in 
#    descending order of popularity

sexes = ['F','M']
babyDict = {(i,j):[] for i in range(2000,2016) for j in sexes}

with open(path) as file:
    for record in file:
        data = record.split(',') 
        year = int(data[0])
        if year in range(2000,2016):          
            babyName = data[1]
            gender = data[2]
            if len(babyDict[(year,gender)])< 20:
                babyDict[(year,gender)].append(babyName)

                
#%%
     
# Define Jaccard function
                    
def getJ(a,b):  
    
    intersection = len(set(a).intersection(set(b)))   
    union = len(set(a+b))
    jaccard = (intersection/union)

    return jaccard

#%%
    
jaccardDict = {i:[] for i in range(2000,2016)}
m = n = []
               
# Cycle through years 2010 - 2015 and create dict of Jaccard similarities
        
for i in range(2000,2016):
    m = list(babyDict[(i, 'F')]) + list(babyDict[(i, 'M')])    
    for j in range(2000,2016):
        n = list(babyDict[(j, 'F')]) + list(babyDict[(j, 'M')])        
        if i != j:                  
            jaccardDict[i].append((j,getJ(m, n)))
            
#%%

# Print similar years
   
for i in range(2000,2016):
    sortedList = list(sorted(jaccardDict[i], key = lambda x : x[1], reverse = True))
    printList = [i]
    for j in range(6):
        printList.append(sortedList[j][0])
    print(printList[0],': ',printList[1:6])
    
#---> Output

'''
2000 :  [2001, 2003, 2002, 2005, 2006]
2001 :  [2000, 2002, 2007, 2003, 2006]
2002 :  [2004, 2003, 2005, 2001, 2006]
2003 :  [2004, 2002, 2005, 2000, 2006]
2004 :  [2005, 2003, 2002, 2006, 2007]
2005 :  [2004, 2006, 2002, 2003, 2009]
2006 :  [2005, 2003, 2004, 2002, 2007]
2007 :  [2008, 2006, 2001, 2004, 2010]
2008 :  [2007, 2011, 2009, 2005, 2004]
2009 :  [2010, 2013, 2011, 2005, 2012]
2010 :  [2009, 2011, 2012, 2008, 2007]
2011 :  [2012, 2010, 2009, 2008, 2013]
2012 :  [2011, 2013, 2010, 2009, 2014]
2013 :  [2014, 2015, 2009, 2012, 2011]
2014 :  [2013, 2015, 2012, 2011, 2010]
2015 :  [2014, 2013, 2011, 2012, 2010]
        
 '''   
    