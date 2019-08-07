
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:31:30 2019

@author: ankusmanish
"""
#function for printing a matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("\t",matrix[i][j],end=" ")
        print("\n")
 
def main():
    m = int( input("enter matrix rows "));
    n = int( input("enter matrix columns "));
    print()
    print('Make sure the both the matrices have same dimesnions ')
    
#declaration of matrices
    matrix_1=[[0 for j in range(n)] for i in range(m)]
    matrix_2=[[0 for j in range(n)] for i in range(m)]
    result=[[0 for j in range(n)] for i in range(m)]
 
#taking input from user
    print ("enter first matrix elements:" )
    for i in range(0 , m):
        for j in range(0 , n):
            matrix_1[i][j]=int (input("enter element "))
    print ("enter second matrix elements:")
    for i in range(0 , m):
        for j in range(0 , n):
            matrix_2[i][j]=int(input("enter element "))
    print ("first matrix")
    print_matrix(matrix_1)
    print ("second matrix")
    print_matrix(matrix_2)
    
    
#loop that adds elements order wise and stores them in matrix result
    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            result[i][j] = matrix_1[i][j] + matrix_2[i][j]
                    
                    
#printing result
    print ( "multiplication of two matrices:" )
    print_matrix(result)
main()