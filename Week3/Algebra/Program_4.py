#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:59:09 2019

@author: ankusmanish
"""

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("\t",matrix[i][j],end = '')
        print("\n")

def main():
    m = int( input("enter first matrix rows "));
    n = int( input("enter first matrix columns "));
    p = int( input("enter second matrix rows "));
    q = int( input("enter second matrix columns "));
    if( n != p):
        print ("matrice multipilication not possible...")
        return 
    
#declaration of matrices
    matrix_1=[[0 for row in range(n)] for col in range(m)]
    matrix_2=[[0 for row in range(q)] for col in range(p)]
    result=[[0 for row in range(q)] for col in range(m)]
 
#taking input from user
    print ("enter first matrix elements:" )
    for i in range(m):
        for j in range(n):
            matrix_1[i][j]=int (input("enter element "))
    print ("enter second matrix elements:")
    for i in range(p):
        for j in range(q):
            matrix_2[i][j]=int(input("enter element "))
    print ("first matrix")
    print_matrix(matrix_1)
    print ("second matrix")
    print_matrix(matrix_2)
    

#for multiplication
    # i will run throgh each row of matrix1
    for i in range(m):
    # j will run through each column of matrix 2
        for j in range(q):
        # k will run throguh each row of matrix 2
            for k in range(0 , n):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j]
                    
#printing result
    print ( "multiplication of two matrices:" )
    print_matrix(result)
main()