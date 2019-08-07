#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:12:13 2019

@author: ankusmanish
"""

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("\t",matrix[i][j],end=" ")
        print("\n")
 
def main():
    m = int( input("enter matrix rows "));
    n = int( input("enter matrix columns "));
    
#declaration of matrices
    matrix_1=[[0 for j in range(n)] for i in range(m)]
    result=[[0 for j in range(m)] for i in range(n)]
 
#taking input from user
    print ("enter first matrix elements:" )
    for i in range(0 , m):
        for j in range(0 , n):
            matrix_1[i][j]=int (input("enter element "))
    print ("first matrix")
    print_matrix(matrix_1)

    
    
#loop that runs through every element and changes the order of the matrix
    # i will run throgh each row of matrix
    for i in range(len(result)):
    # j will run through each column of matrix 
        for j in range(len(result[0])):
            result[i][j] = matrix_1[j][i]
                    
                    
#printing result
    print ( "multiplication of two matrices:" )
    print_matrix(result)
main()