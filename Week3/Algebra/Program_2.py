#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:44:29 2019

@author: ankusmanish
"""

#function for printing a matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("\t",matrix[i][j],end = '')
        print("\n")

def main():
    m = int( input("enter matrix rows "));
    n = int( input("enter matrix columns "));
    p = int(input("Enter the number "))
    
#declaration of matrices
    matrix_1=[[0 for row in range(n)] for col in range(m)]
    result=[[0 for row in range(n)] for col in range(m)]
 
#taking input from user
    print ("enter matrix elements:" )
    for i in range(m):
        for j in range(n):
            matrix_1[i][j]=int (input("enter element "))
    print ("Given matrix")
    print_matrix(matrix_1)

    

#loop that multiplies every element in the matrix with the given number
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[0])):
            result[i][j] += matrix_1[i][j] * p
                    
#printing result
    print ( "multiplication of matrix is : ")
    print_matrix(result)
main()
