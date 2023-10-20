import random
import numpy as np

def ex1():
    vect = np.arange(0,21 )
    print("Original vector :")
    print(vect)
    for i in range(9,15):
        vect[i] = -vect[i]
    print("\nVector changed :")
    print(vect)

def ex2():
    vect = np.arange(15,56)
    print("Original vector :")
    print(vect)
    L = []
    for i in range(1, len(vect)-1):
        L.append(vect[i])
    print("\nVector changed :")
    L = np.array(L)
    print(L)

def ex3():
    x1 = int(input("Enter the minimum value of the matrix : "))
    x2 = int(input("Enter the maximum value of the matrix : "))
    mat = np.random.randint(x1,x2, size=(3,4))
    print(mat)
    
def ex4():
    vect = np.linspace(5,50,10)
    print(vect)

def ex5():
    mat = np.random.randint(0,11, size=5)
    print(mat)
    
def ex6():
    A =  np.random.randint(0,11, size=5)
    B =  np.random.randint(0,11, size=5)
    print("A : {}".format(A))
    print("\nB : {}".format(B))
    C = np.matmul(A,B)
    print("\nAB : {} ".format(C))
    
def ex7():
    mat = np.random.randint(10,22, size=(3,4))
    print(mat)

def ex8():
    mat = np.random.randint(10,22, size=(3,4))
    print(mat)
    row = len(mat)
    col = len(mat[0])
    print("\nrow : {}".format(row))
    print("col : {}".format(col))
    
def ex9():
    mat = np.zeros((4,4))
    k = 1
    for i in range(4):
        for j in range(4):
            if i == j:
                None
            else:
                if k ==2:
                    mat[i][j]=1
            k = 3 - k
    print(mat)


def ex10():
    Array1 = np.array([0, 10, 20, 40, 60])
    Array2 = np.array([10, 30, 40])
    L = []
    res = []
    for i in range(len(Array1)):
        for j in range(len(Array2)):
            if Array1[i] == Array2[j]:
                L.append(Array1[i])
    
                
    print("Array1 : {}".format(Array1))
    print("Array2 : {}".format(Array2))
    print("\nCommon values between two arrays : ")
    print(L)


def ex11():
    array1 = np.array([10,10,20,20,30,30])
    array2 = np.array([[1,1],[2,3]])
    L1 = []
    L2 = []
    
    for i in range(len(array1)):
        if array1[i] in L1:
            None
        else:
            L1.append(array1[i])
    print("Original array : \n{}".format(array1))
    print("Unique elements of the above array : \n{}".format(L1))
    
    
    for j in range(len(array2)):
        for k in range(len(array2[0])):
            if array2[j][k] in L2:
                None
            else:
                L2.append(array2[j][k])
    print("\nOriginal array : \n{}".format(array2))
    print("Unique elements of the above array : \n{}".format(L2))
    
def ex12():    
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([4, 5, 6])
    
    cross_product = np.cross(vector1, vector2)
    
    print("Vector 1:", vector1)
    print("Vector 2:", vector2)
    print("Cross Product:", cross_product)

def ex13():
    cartesian = np.random.rand(10, 2)
    
    r = np.sqrt(cartesian[:, 0]**2 + cartesian[:, 1]**2)
    theta = np.arctan2(cartesian[:, 1], cartesian[:, 0])
    
    print(r)
    print(theta)



def ex14():
    vect = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
        20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 
        38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 
        56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 
        74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 
        92, 93, 94, 95, 96, 97, 98, 99])
    
    value = float(input("Enter the value to compare : "))
    
    L = np.zeros(len(vect))
    
    for i in range(len(vect)):
        if vect[i]>=value:
            L[i]=vect[i]-value
        else:
            L[i]=value-vect[i]
            
    print(vect[L.argmin()])
    
    






































































