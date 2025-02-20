# import sys
import array
import math
import sympy # used for prime numbers
import numpy as np

### constants
pi  = 3.1415926535897932384626
e   = 2.7182818284593451253602

#region arithmetics
def add(num1, num2):
    res = num1 + num2
    print(f'{num1} + {num2} = {res}')
    return res

def subtract(num1, num2):
    res = num1 - num2
    print(f'{num1} - {num2} = {res}')
    return res

def multiply(num1, num2):
    res = num1 * num2
    print(f'{num1} * {num2} = {res}')
    return res

def divide(num1, num2):
    if num2 != 0:
        res = num1 / num2
        print(f'{num1} / {num2} = {res}')
        return num1 / num2
    else:
        print("*~Illegal division: n/0... solving as = 0~*")
        return 0

def simplifyFraction(num1, num2): # seems good
    if num1 >= num2:
        num3 = num1
    else:
        num3 = num2

    primeList = list(sympy.primerange(0, num3))
    primeList.reverse()

    for prime in primeList:
        temp1 = num1
        temp2 = num2

        temp1 /= prime
        temp2 /= prime

        if temp1 == int(temp1) and temp2 == int(temp2):
            print("dividing", num1, "and", num2, "with", prime)
            num1 /= prime
            num2 /= prime

            print(f'\t = {num1} / {num2}')

            if int(num1) == 1:
                return num1, num2
            else:
                #print(f'Simplifying {num1} / {num2}')
                return simplifyFraction(num1, num2)
            
    print(f'Simplest fraction is: {num1} / {num2}')
    return num1, num2

def exponent(num1, num2): # works, also with negative numbers, and decimal
    # I think there is an easier way for this ?
    num1 = num1 # well yeah, duh
    num2 = num2 # -||-
    num3 = num1

    if num1 != int(num1) or num2 != int(num2): # whatever happens here is slightly wrong(precision error)
        # sets the exponent to decimal places
        num2 = round(num2, 10000)
        num2 *= 100000 # change this number to increase accuracy
        num2 = int(num2)

        # simplify fraction (just make that another function)
        num1 = root(num1, 100000)
        num3 = num1

        for i in range(1, num2): #is this just a repeat? (last else statement)
            num3 *= num1
        return num3
    
    elif num1 == 0 and num2 == 0:
        print("*~Illegal operation: 0^0... solving as = 0~*")
        return 0
    
    elif num1 == 0 and num2 != 0:
        return 0
    
    elif num1 != 0 and num2 == 0:
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
    res = math.pow(num1, 1.0/num2)

    return res

# region trigonometry 
###(multiple definitions based on the parameters. angles, length, (radian))
def pythagoras(num1, num2):
    num3 = exponent(num1, 2) + exponent(num2, 2)
    res = root(num3, 2)

    return res

def sin(**kwargs): # we only know 2 of the values..
    #angle, opposite, hypotenuse

    angle = kwargs.get('angle')
    opp = kwargs.get('opp')
    adj = kwargs.get('adj')
    hyp = kwargs.get('hyp')

    print("yo! im sin")
    return 'not numbers here yet :)'

def cos(**kwargs):
    #angle, adjacent, hypotenuse
    print("yo! im cos")

def tan(**kwargs):
    #angle, opposite, adjacent
    print("yo! im tan")

def cosecant(**kwargs):
    #angle, hypotenuse, opposite
    print("yo! im cosecant")

def secant(**kwargs):
    #angle, hypotenuse, adjacent
    print("yo! im secant")

def cotangent(**kwargs):
    #angle, adjacent, opposite
    print("yo! im cotangent")

def arcSin(**kwargs):
    #angle, opposite, hypotenuse
    print("yo! im arcSin")

def arcCos(**kwargs):
    #angle, adjacent, hypotenuse
    print("yo! im arcCos")

def arcTan(**kwargs):
    #angle, opposite, adjacent
    print("yo! im arcTan")

# endregion
# region vectors
def vect(*values):
    vect = [i for i in values]

    if len(vect) < 2: 
        print("\t*~please specify 2 or more vector values~*")

    return vect

def vectLenght(vect): # like 95% correct (more like 99% now :>)
    #length = 0
    exponents = 0
    
    for i in range(len(vect)):
        #length = pythagoras(vect[i], vect[i + 1]) # lol wrong
        exponents += exponent(vect[i], 2)
        
    length = root(exponents, 2)
    print(f'\u221A{exponents} = {length}')

    return length

def vectSum(*values):
    vector_list = [i for i in values]
    vectRes = [0] * len(vector_list[0])

    for i in range(len(vector_list)):
        for j in range(len(vector_list[0])):
            vectRes[i] += vector_list[j][i]

    return vectRes

def transpose(vect1):
    vect2 = np.zeros((len(vect1), 1))

    for i in range(len(vect1)):
        vect2[i][0] = vect1[i]

    return vect2

def project(vect1, vect2):
    projection = dotProduct(vect1, vect2) / pythagoras(vect2[0], vect2[1])
    return projection

def dotProduct(*values):
    vector_list = [i for i in values]
    scalar = 0
    
    if (len(vector_list) != 2):
        print('please only put 2 numbers or objects')
        return False
    
    if (len(vector_list[0]) != len(vector_list[1])):
        print('objects are not of same length')
        return False

    for i in range(len(vector_list[0])):
        parenthesis = 1

        for j in range(len(vector_list)): 
            parenthesis *= vector_list[j][i]

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

# region matrices 
### make dynamic for loops for more dimensions pls
def matrixPlus(mat1, mat2): # please only use 2 dimensions :)
    if len(mat1) == len(mat2):
        mat3 = mat1

        print(f'{mat1} + {mat2}')

        for i in range(len(mat1)):
            for j in range(len(mat1[i])):
                mat3[i][j] = mat1[i][j] + mat2[i][j]
                print(f'{i},{j} = {mat3[i][j]}')
        return mat3
    else:
        print("can't add matrices of different dimensions...")

def matrixMinus(mat1, mat2): # please only use 2 dimensions :)
    if len(mat1) == len(mat2):
        mat3 = mat1

        print(f'{mat1} - {mat2}')

        for i in range(len(mat1)):
            for j in range(len(mat1[i])):
                mat3[i][j] = mat1[i][j] - mat2[i][j]
                print(f'{i},{j} = {mat3[i][j]}')
        return mat3
    else:
        print("can't subtract matrices of different dimensions...")

def matrixMult(mat1, mat2): # please only use 2 dimensions (or more idc) :)
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)

    if (mat1.shape[0] != mat2.shape[1] or mat1.shape[1] != mat2.shape[0]):
        print('Matrix dimensions does not fit!')
        return False

    rows = 1
    coloums = 1

    if (mat1.shape[0] > mat2.shape[0]):
        rows = mat1.shape[0]
    else:
        rows = mat2.shape[0]

    if (mat1.shape[1] > mat2.shape[1]):
        coloums = mat1.shape[1]
    else:
        coloums = mat2.shape[1]

    mat3 = np.zeros((rows, coloums))
    mat2 = flipMatrix(mat2)

    for i in range(len(mat3)):
        for j in range(len(mat3)):
            mat3[i][j] = dotProduct(mat1[i], mat2[j])

    print(f'{mat1} * {mat2} = {mat3}')

    return mat3

def matrixDiv(mat1, mat2): # please only use 2 dimensions :)
    # the internet does not like to divide matrices, so I won't either
    return 1

def flipMatrix(mat1):
    coloums = len(mat1)
    rows = len(mat1[0])

    mat2 = np.zeros((rows, coloums))

    for i in range(len(mat2)):
        for j in range(len(mat2[0])):
            mat2[j][i] = mat1[i][j]
    #print(f'{mat2=}')

    return mat2

def inverseMatrix(mat1):
    #https://www.emathhelp.net/calculators/linear-algebra/inverse-of-matrix-calculator/?i=%5B%5B1%2C1%2C1%5D%2C%5B2%2C3%2C4%5D%2C%5B3%2C1%2C1%5D%5D
    return 1

# endregion
# region calculus
def differential():
    return 1

def integral():
    return 1

def multiVariableCalculus():
    return 1

# endregion
# region logarihtmic
def logarithm():
    print("yo! im a log")

def nLogarithm():
    print("yo! im a tree")

# endregion
##########################################
# region equations
#equation = divide(7423,852)
#equation = simplifyFraction(12,500)
#equation = exponent(5,5.8)
#equation = root(234,3.3)
#equation = vectLenght(vect(45,265,79,3))
equation = sin(1,None,2)
#equation = determinant(vect(1,2,3), vect(4,5,6))
#equation = transpose(vect(4,5,6,8))
#equation = flipMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#equation = dotProduct(vect(3,1,3,5), vect(2,3,8,2))
#equation = matrixMult([[1,2,3],[4,5,6],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]])
print("Equation =\n\t", str(equation))

def iToPowerOfPi():
    for i in range(1, 11):
        equation = exponent(i, pi)

        print("Equation", i, "=\n\t", str(equation), "\n")
#iToPowerOfPi()

# nice way to test values
#print(f'{equation=}')


'''
arithmetics
(pre-)algebra
trigonometry
geometry?
pre-calc
vector
matrices
calculus
logarithmic
integrated math

equations

dont print the final equation result, print the temporary result, and pass it back?
'''
