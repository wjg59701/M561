# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:14:14 2019

@author: Bill Griffin

------------------------------- Homework 1 
------------------------------- Problem 1

"""
def compute_factors(r):

# Initialize a dictionary with keys 1 to r and 
# value of 1 since 1 is a factor of everything

    factorsDict = {n:1 for n in range(1,r+1)}

    for n in factorsDict.keys():                     # Iterate through numbersDict
        factorList = []                             # Initialize/reset factor list
        for factor in range(1,n+1):                    # Loop from 1 to the number
            if n%factor == 0:               # If remainder is 0 it is a factor ...
                factorList.append(factor)       # ... so append it to the list ...
                factorsDict[n] = factorList                 # and put the list factorsDict
    return factorsDict

#%%
# Print the last 50
    
factorsDict = compute_factors(10000)
       
for n in range(9951,10001):
    print('The factors of ', n, 'are', factorsDict[n])

# Output --------------->
    
'''    
The factors of  9951 are [1, 3, 31, 93, 107, 321, 3317, 9951]
The factors of  9952 are [1, 2, 4, 8, 16, 32, 311, 622, 1244, 2488, 4976, 9952]
The factors of  9953 are [1, 37, 269, 9953]
The factors of  9954 are [1, 2, 3, 6, 7, 9, 14, 18, 21, 42, 63, 79, 126, 158, 237, 474, 553, 711, 1106, 1422, 1659, 3318, 4977, 9954]
The factors of  9955 are [1, 5, 11, 55, 181, 905, 1991, 9955]
The factors of  9956 are [1, 2, 4, 19, 38, 76, 131, 262, 524, 2489, 4978, 9956]
The factors of  9957 are [1, 3, 3319, 9957]
The factors of  9958 are [1, 2, 13, 26, 383, 766, 4979, 9958]
The factors of  9959 are [1, 23, 433, 9959]
The factors of  9960 are [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 83, 120, 166, 249, 332, 415, 498, 664, 830, 996, 1245, 1660, 1992, 2490, 3320, 4980, 9960]
The factors of  9961 are [1, 7, 1423, 9961]
The factors of  9962 are [1, 2, 17, 34, 293, 586, 4981, 9962]
The factors of  9963 are [1, 3, 9, 27, 41, 81, 123, 243, 369, 1107, 3321, 9963]
The factors of  9964 are [1, 2, 4, 47, 53, 94, 106, 188, 212, 2491, 4982, 9964]
The factors of  9965 are [1, 5, 1993, 9965]
The factors of  9966 are [1, 2, 3, 6, 11, 22, 33, 66, 151, 302, 453, 906, 1661, 3322, 4983, 9966]
The factors of  9967 are [1, 9967]
The factors of  9968 are [1, 2, 4, 7, 8, 14, 16, 28, 56, 89, 112, 178, 356, 623, 712, 1246, 1424, 2492, 4984, 9968]
The factors of  9969 are [1, 3, 3323, 9969]
The factors of  9970 are [1, 2, 5, 10, 997, 1994, 4985, 9970]
The factors of  9971 are [1, 13, 59, 169, 767, 9971]
The factors of  9972 are [1, 2, 3, 4, 6, 9, 12, 18, 36, 277, 554, 831, 1108, 1662, 2493, 3324, 4986, 9972]
The factors of  9973 are [1, 9973]
The factors of  9974 are [1, 2, 4987, 9974]
The factors of  9975 are [1, 3, 5, 7, 15, 19, 21, 25, 35, 57, 75, 95, 105, 133, 175, 285, 399, 475, 525, 665, 1425, 1995, 3325, 9975]
The factors of  9976 are [1, 2, 4, 8, 29, 43, 58, 86, 116, 172, 232, 344, 1247, 2494, 4988, 9976]
The factors of  9977 are [1, 11, 907, 9977]
The factors of  9978 are [1, 2, 3, 6, 1663, 3326, 4989, 9978]
The factors of  9979 are [1, 17, 587, 9979]
The factors of  9980 are [1, 2, 4, 5, 10, 20, 499, 998, 1996, 2495, 4990, 9980]
The factors of  9981 are [1, 3, 9, 1109, 3327, 9981]
The factors of  9982 are [1, 2, 7, 14, 23, 31, 46, 62, 161, 217, 322, 434, 713, 1426, 4991, 9982]
The factors of  9983 are [1, 67, 149, 9983]
The factors of  9984 are [1, 2, 3, 4, 6, 8, 12, 13, 16, 24, 26, 32, 39, 48, 52, 64, 78, 96, 104, 128, 156, 192, 208, 256, 312, 384, 416, 624, 768, 832, 1248, 1664, 2496, 3328, 4992, 9984]
The factors of  9985 are [1, 5, 1997, 9985]
The factors of  9986 are [1, 2, 4993, 9986]
The factors of  9987 are [1, 3, 3329, 9987]
The factors of  9988 are [1, 2, 4, 11, 22, 44, 227, 454, 908, 2497, 4994, 9988]
The factors of  9989 are [1, 7, 1427, 9989]
The factors of  9990 are [1, 2, 3, 5, 6, 9, 10, 15, 18, 27, 30, 37, 45, 54, 74, 90, 111, 135, 185, 222, 270, 333, 370, 555, 666, 999, 1110, 1665, 1998, 3330, 4995, 9990]
The factors of  9991 are [1, 97, 103, 9991]
The factors of  9992 are [1, 2, 4, 8, 1249, 2498, 4996, 9992]
The factors of  9993 are [1, 3, 3331, 9993]
The factors of  9994 are [1, 2, 19, 38, 263, 526, 4997, 9994]
The factors of  9995 are [1, 5, 1999, 9995]
The factors of  9996 are [1, 2, 3, 4, 6, 7, 12, 14, 17, 21, 28, 34, 42, 49, 51, 68, 84, 98, 102, 119, 147, 196, 204, 238, 294, 357, 476, 588, 714, 833, 1428, 1666, 2499, 3332, 4998, 9996]
The factors of  9997 are [1, 13, 769, 9997]
The factors of  9998 are [1, 2, 4999, 9998]
The factors of  9999 are [1, 3, 9, 11, 33, 99, 101, 303, 909, 1111, 3333, 9999]
The factors of  10000 are [1, 2, 4, 5, 8, 10, 16, 20, 25, 40, 50, 80, 100, 125, 200, 250, 400, 500, 625, 1000, 1250, 2000, 2500, 5000, 10000]

'''
#%%
# M561 Problem -----Part 1---- BUILD A DICTIONARY OF PRIME FACTORS-------->

def isPrime(n, factorsDict):
    if len(factorsDict[n]) <= 2:
        return True
    return False
    
primes_dict = {}

for i in range(1,10001):
    for j in range(len(factorsDict[i])):
        m = isPrime(factorsDict[i][j],factorsDict)
        if m == True:
            try:
                primes_dict[i].append(factorsDict[i][j])
            except:
                primes_dict[i] = [factorsDict[i][j]]  
                
for n in range(9951,10001):
    print('The prime factors of ', n, 'are', primes_dict[n])
           
# Output -------->

'''
The prime factors of  9951 are [1, 3, 31, 107]
The prime factors of  9952 are [1, 2, 311]
The prime factors of  9953 are [1, 37, 269]
The prime factors of  9954 are [1, 2, 3, 7, 79]
The prime factors of  9955 are [1, 5, 11, 181]
The prime factors of  9956 are [1, 2, 19, 131]
The prime factors of  9957 are [1, 3, 3319]
The prime factors of  9958 are [1, 2, 13, 383]
The prime factors of  9959 are [1, 23, 433]
The prime factors of  9960 are [1, 2, 3, 5, 83]
The prime factors of  9961 are [1, 7, 1423]
The prime factors of  9962 are [1, 2, 17, 293]
The prime factors of  9963 are [1, 3, 41]
The prime factors of  9964 are [1, 2, 47, 53]
The prime factors of  9965 are [1, 5, 1993]
The prime factors of  9966 are [1, 2, 3, 11, 151]
The prime factors of  9967 are [1, 9967]
The prime factors of  9968 are [1, 2, 7, 89]
The prime factors of  9969 are [1, 3, 3323]
The prime factors of  9970 are [1, 2, 5, 997]
The prime factors of  9971 are [1, 13, 59]
The prime factors of  9972 are [1, 2, 3, 277]
The prime factors of  9973 are [1, 9973]
The prime factors of  9974 are [1, 2, 4987]
The prime factors of  9975 are [1, 3, 5, 7, 19]
The prime factors of  9976 are [1, 2, 29, 43]
The prime factors of  9977 are [1, 11, 907]
The prime factors of  9978 are [1, 2, 3, 1663]
The prime factors of  9979 are [1, 17, 587]
The prime factors of  9980 are [1, 2, 5, 499]
The prime factors of  9981 are [1, 3, 1109]
The prime factors of  9982 are [1, 2, 7, 23, 31]
The prime factors of  9983 are [1, 67, 149]
The prime factors of  9984 are [1, 2, 3, 13]
The prime factors of  9985 are [1, 5, 1997]
The prime factors of  9986 are [1, 2, 4993]
The prime factors of  9987 are [1, 3, 3329]
The prime factors of  9988 are [1, 2, 11, 227]
The prime factors of  9989 are [1, 7, 1427]
The prime factors of  9990 are [1, 2, 3, 5, 37]
The prime factors of  9991 are [1, 97, 103]
The prime factors of  9992 are [1, 2, 1249]
The prime factors of  9993 are [1, 3, 3331]
The prime factors of  9994 are [1, 2, 19, 263]
The prime factors of  9995 are [1, 5, 1999]
The prime factors of  9996 are [1, 2, 3, 7, 17]
The prime factors of  9997 are [1, 13, 769]
The prime factors of  9998 are [1, 2, 4999]
The prime factors of  9999 are [1, 3, 11, 101]
The prime factors of  10000 are [1, 2, 5]

'''

#%%

# M561 Problem -----Part 2 ----COUNT AND REPORT THE NUMBER ----
#                         OF PRIME NUMBERS <10,000 <100,000 ---

factorsDict = compute_factors(100000)

#%%

c= 0

run = [10001,100001]

for i in run:
    for j in range(2,i):
        m = isPrime(j,factorsDict)
        if m == True:
            c += 1
        
    print('There are ',c,' primes between 2 and ', i-1)
    c = 0
    
# Output --->
    
'''
There are  1229  primes between 2 and  10000
There are  9592  primes between 2 and  100000
'''    

    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    