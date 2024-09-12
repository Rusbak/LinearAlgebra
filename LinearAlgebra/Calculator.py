# import sys
import array
import math
import sympy # used for prime numbers
import numpy as np

### constants
pi  = 3.1415926535897932384626
e   = 2.7182818284593451253602

### basics
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("*~Illegal division: n/0... solving as = 0~*")
        return 0

###
def simplifyFraction(num1, num2):
    if num1 >= num2:
        num3 = num1
    else:
        num3 = num2

    primeList = list(sympy.primerange(0, num3))
    primeList.reverse()
    print(type(primeList), list(primeList))

    for prime in primeList:
        print(prime)
        temp1 = num1 # temp1, temp2 = num1, num2
        temp2 = num2

        temp1 /= prime
        temp2 /= prime

        if temp1 == int(temp1) and temp2 == int(temp2):
            num1 /= prime
            num2 /= prime
            print("dividing", num1, num2, "with", prime)
            simplifyFraction(num1, num2)

    return num1, num2

def exponent(num1, num2): # does not work with negative numbers
    # I think there is an easier way for this ?
    num1 = num1
    num2 = num2
    num3 = num1
    if num1 != int(num1) or num2 != int(num2):  # whatever happens here is slightly wrong
        # sets the exponent to decimal places
        num2 = round(num2, 10000)
        num2 *= 100000 # change this number to increase accuracy
        num2 = int(num2)

        # simplify fraction (just make that another function)
        num1 = root(num1, 100000)
        num3 = num1

        for i in range(1, num2):
            num3 *= num1
        return num3
    elif num1 == 0 and num2 == 0:
        print("*~Illegal operation: 0^0... solving as = 0~*")
        return 0
    elif num1 == 0 and num2 != 0:
        return 0
    elif num2 == 0 and num1 != 0:
        return 1
    else:
        if num2 > 0:
            for i in range(1, num2):
                num3 *= num1
        elif num2 < 0:
            for i in range(num2, 1):
                num3 /= num1
        return num3

def root(num1, num2):
    # can't figure this shit out, imma just use .math function here
    # shhh don't tell anyone that im just calculating the inverse exponent
    num1 = math.pow(num1, 1.0/num2)

    return num1

### trigonometry (multiple definitions based on the parameters. angles, length, (radian))
def pythagoras(num1, num2):
    num3 = exponent(num1, 2) + exponent(num2, 2)
    res = root(num3, 2)

    return res

def sin():
    print("yo! im sin")

def cos():
    print("yo! im cos")

def tan():
    print("yo! im tan")

def arcSin():
    print("yo! im arcSin")

def arcCos():
    print("yo! im arcCos")

def arcTan():
    print("yo! im arcTan")


### vectors
def vect(*values):
    vect = [i for i in values]
    if len(vect) < 2: print("\t*~please specify 2 or more vector values~*")
    return vect

def vectLenght(vect): # like 95% correct
    length = 0
    for i in range(len(vect)-1):
        length = pythagoras(vect[i], vect[i+1])
    return length

def vectSum(*values):
    vector_list = [i for i in values]
    vectRes = [0] * len(vector_list[0])

    for i in range(len(vector_list)):
        for j in range(len(vector_list[0])):
            vectRes[i] += vector_list[j][i]
    return vectRes

def project(vect1, vect2):
    projection = dotProduct(vect1, vect2) / pythagoras(vect2[0], vect2[1])
    return projection

def dotProduct(*values):
    vector_list = [i for i in values]
    scalar = 0

    for i in range(len(vector_list)):
        parenthesis = 1
        for j in range(len(vector_list[0])):
            parenthesis *= vector_list[j][i]
        print(parenthesis)
        scalar += parenthesis
    return scalar

def vectxScalar(vect, scalar):
    res = vect
    for i in range(len(res)):
        res[i] = vect[i] * scalar
    return res

def betweenVect(vect1, vect2):
    res = vect1
    for i in range(len(res)):
        res[i] = vect2[i] - vect1[i]
    return res

def crossProduct(vect1, vect2):
    res = [0] * len(vect1)

    if (len(vect1) or len(vect2)) != 3:
        print(len(vect1), len(vect2))
        print("\t*~crossproduct are only possible in 3D and 7D spaces~*")
        return
    else:
        for i in range(len(res)):
            index = i
            res[index] = vect1[index-2] * vect2[index-1] - vect1[index-1] * vect2[index-2]
        return res

def determinant(vect1, vect2):
    res = 0
    if len(vect1) != len(vect2):
        print("vectors are different dimensions")
        return
    elif (len(vect1) or len(vect2)) != 2:
        print("\t*~determinant are only for 2D vectors. Calculating cross product~*")
        res = crossProduct(vect1, vect2)
    else:
        res += vect1[0] * vect2[1] - vect1[1] * vect2[0]
    return res

### matrices (make dynamic for loops for more dimensions pls
def matrixPlus(mat1, mat2): # please only use 2 dimensions :)
    if len(mat1) == len(mat2):
        mat3 = mat1
        for i in range(len(mat1)):
            for j in range(len(mat1[i])):
                mat3[i][j] = mat1[i][j] + mat2[i][j]
        return mat3
    else:
        print("can't add matrices of different dimensions...")

def matrixMinus(mat1, mat2): # please only use 2 dimensions :)
    if len(mat1) == len(mat2):
        mat3 = mat1
        for i in range(len(mat1)):
            for j in range(len(mat1[i])):
                mat3[i][j] = mat1[i][j] - mat2[i][j]
        return mat3
    else:
        print("can't add matrices of different dimensions...")

### derivatives
def differential():
    return 1

def integral():
    return 1

### logarihtmic functions
def logarithm():
    print("yo! im a log")

##########################################

equation = determinant(vect(1,2,3,),vect(4,5,6))
print("Equation =\n\t", str(equation))


def iToPowerOfPi():
    for i in range(1, 11):
        equation = exponent(i, pi)

        print("Equation", i, "=\n\t", str(equation), "\n")
#iToPowerOfPi()