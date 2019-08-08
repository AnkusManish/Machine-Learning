#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:01:49 2019

@author: ankusmanish
"""

X=[[12,7,3],
   [4,5,6],
   [7,8,9]]

#result creates empty lists
result=[ ]
for i in range(len(X)):
    result.append([ ])
    
#creating a zero matrix result    
for i in range(len(X)):
    for j in range(len(X)):
        result[i].append(0)
        
        
#Finding the determinant of the given matrix        
a=(X[0][0]*((X[1][1]*X[2][2])-(X[1][2]*X[2][1])))
b=-(X[0][1]*((X[1][0]*X[2][2])-(X[2][0]*X[1][2])))
c=(X[0][2]*((X[1][0]*X[2][1])-(X[2][0]*X[1][1])))

det=a+b+c

#finding adjoint of a given matrix
A11=(X[1][1]*X[2][2])-(X[2][1]*X[1][2])
A12=-((X[1][0]*X[2][2])-(X[1][2]*X[2][0]))
A13=(X[1][0]*X[2][1])-(X[2][0]*X[1][1])
A21=-((X[0][1]*X[2][2])-(X[2][1]*X[0][2]))
A22=(X[0][0]*X[2][2])-(X[2][0]*X[0][2])
A23=-((X[0][0]*X[2][1])-(X[0][1]*X[2][0]))
A31=(X[0][1]*X[1][2])-(X[1][1]*X[0][2])
A32=-((X[0][0]*X[1][2])-(X[1][0]*X[0][2]))
A33=(X[0][0]*X[1][1])-(X[1][0]*X[0][1])

#storing adjoint elements in a matrix Y
Y=[[A11,A21,A31],
   [A12,A22,A32],
   [A13,A23,A33]]

#Calculating the determinant value
determinant=1/det


#loop that fills the result matrix with adjoint values
for i in range(len(X)):
    for j in range(len(X)):
        result[i][j]=determinant*Y[i][j]
        
#printing the result matrix
for i in result:
    print(i)        
