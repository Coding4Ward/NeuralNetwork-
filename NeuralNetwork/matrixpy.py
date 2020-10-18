#-*-coding:utf8;-*-
import random

def add(m1, m2):
    # Escalar addition: Matrix + Number
    if typeOf(m1)==1 and (typeOf(m2)==2 or typeOf(m2)==3 or typeOf(m2)==4):
       matrix = zeros(len(m1), len(m1[0]))
       for rows in range(len(m1)):
           for cols in range(len(m1[0])):
               matrix[rows][cols] = m1[rows][cols] + m2
       return matrix
    # Escalar addition: Number + Matrix
    elif typeOf(m2)==1 and (typeOf(m1)==2 or typeOf(m1)==3 or typeOf(m1)==4):
       matrix = zeros(len(m2), len(m2[0]))
       for rows in range(len(m2)):
           for cols in range(len(m2[0])):
               matrix[rows][cols] = m1 + m2[rows][cols]
       return matrix
    # Escalar addition: Array + Number
    elif typeOf(m1)==0 and (typeOf(m2)==2 or typeOf(m2)==3 or typeOf(m2)==4):
         added = zeros(len([m1]), len([m1][0]))
         for rows in range(len([m1])):
             for cols in range(len([m1][0])):
                 added[rows][cols] = [m1][rows][cols] + m2
         return fromMatrix(added)
    # Escalar addition: Number + Array
    elif typeOf(m2)==0 and (typeOf(m1)==2 or typeOf(m1)==3 or typeOf(m1)==4):
         added = zeroz(len([m2]), len([m2][0]))
         for rows in range(len([m2])):
             for cols in range(len([m2][0])):
                 added[rows][cols] = [m2][rows][cols] + m1
         return fromMatrix(added)
    # Array + Array
    elif typeOf(m1)==0 and typeOf(m2)==0: #It's an array
         added = zeros(len([m1]), len([m1][0]))
         for rows in range(len([m1])):
             for cols in range(len([m1][0])):
                 added[rows][cols] = [m1][rows][cols] + [m2][rows][cols]
         return fromMatrix(added)
    # The real addition of two matrix: Matrix + Matrix
    elif typeOf(m1)==1 and typeOf(m2)==1: # Matrix + Matrix
         if len(m1)!=len(m2) and len(m1[0])!=len(m2[0]): return []
         matrix = zeros(len(m1), len(m2[0]))
         for rows in range(len(m1)):
             for cols in range(len(m2[0])):
                 matrix[rows][cols] = m1[rows][cols] + m2[rows][cols]
         return matrix
    else: return []
    
def array(nelements):
    return [0]*nelements

def transpose(matrix):
    """Transpose a matrix, turn rows into cols."""
    if typeOf(matrix)==1:
       transposed = zeros(len(matrix[0]), len(matrix))
       for rows in range(len(matrix)):
           for cols in range(len(matrix[0])):
               transposed[cols][rows] = matrix[rows][cols]
       return transposed
    elif typeOf(matrix)==0:
         return [matrix]
    return "The <object> isn't an array or a matrix"
    
def oppose(matrix):
    """Oppose a matrix value, turn all positive values into negate and vice verse."""
    matrix_type = typeOf(matrix)
    try:
       if matrix_type==1:
          opposed = zeros(len(matrix), len(matrix[0]))
          for rows in range(len(matrix)):
              for cols in range(len(matrix[0])):
                  opposed[rows][cols] = -matrix[rows][cols]
          return opposed
       else:
           opposed = zeros(len([matrix]), len([matrix][0]))
           for rows in range(len([matrix])):
               for cols in range(len([matrix][0])):
                   opposed[rows][cols] = -[matrix][rows][cols]
           return fromMatrix(opposed)
    except Exception as error:
          return "The <object> isn't an array or a matrix"
          
def typeOf(obj):
    """Verify if obj is an array, a matrix, a number, or a string."""
    try:
        n_cols = len(obj[0]) # Try take the number of cols of the obj
        if type(obj)==str: return 5 # If the obj is a string
        else: return 1 # If the obj is a Matrix
    except Exception as error:
        if type(obj)==list: return 0 # If the obj is an array
        elif type(obj)==int: return 2 # If the obj is an Integer number
        #elif type(obj)==long: return 3 # If the obj is a long number
        elif type(obj)==float: return 4 # If the obj is a float number
        else: return -1 # If the obj is an Float number
               
def fromMatrix(matrix):
    """Turn a matrix into an Array."""
    if typeOf(matrix) != 1: return "The <object> isn't a matrix"
    array = []
    for rows in range(len(matrix)):
        for cols in range(len(matrix[0])):
            array.append(matrix[rows][cols])
    return array

def fromArray(array):
    """Turn an array into a matrix."""
    if typeOf(array) != 0: return "The <object> isn't an array"
    matrix = zeros(len([array][0]), len([array]))
    for rows in range(len([array])):
        for cols in range(len([array][0])):
            matrix[cols][rows] = [array][rows][cols]
    return matrix
                      
def show(matrix):
    """Print a matrix with '|' as bracket."""
    if typeOf(matrix) == 1:
       for rows in matrix:
           m = str(rows).replace("[","|")
           m = m.replace("]","|")
           print(m)
       print("\n")
       
def zeros(nrows, ncols):
    matrix = []
    for rows in range(nrows):
        newline = [0]*ncols
        matrix.append(newline)
    return matrix
    

def hadamard(m1, m2):
    if typeOf(m1)==0 and typeOf(m2)==0: #Array
       if len(m1)==len(m2):
          hadamardArray = array(len(m1))
          for i in range(len(m1)):
              hadamardArray[i] = m1[i] * m2[i]
          return hadamardArray
       return []
           
    elif typeOf(m1)==1 and typeOf(m2)==1: #Matrix
         if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
            hadamardMatrix = zeros(len(m1), len(m1[0]))
            for rows in range(len(m1)):
                for cols in range(len(m1[0])):
                    hadamardMatrix[rows][cols] = m1[rows][cols] * m2[rows][cols]
            return hadamardMatrix
         return []
    else: return []
    
def multiply(m1, m2):
    # Escalar multiplication: Matrix * Number
    if typeOf(m1)==1 and (typeOf(m2)==2 or typeOf(m2)==3 or typeOf(m2)==4):
       matrix = zeros(len(m1), len(m1[0]))
       for rows in range(len(m1)):
           for cols in range(len(m1[0])):
               matrix[rows][cols] = m1[rows][cols] * m2
       return matrix
    # Escalar multiplication: Number * Matrix
    elif typeOf(m2)==1 and (typeOf(m1)==2 or typeOf(m1)==3 or typeOf(m1)==4):
       matrix = zeros(len(m2), len(m2[0]))
       for rows in range(len(m2)):
           for cols in range(len(m2[0])):
               matrix[rows][cols] = m1 * m2[rows][cols]
       return matrix
    
    # The real multiplication
    elif typeOf(m1)==1 and typeOf(m2)==1: # Matrix * Matrix
         if len(m1[0]) != len(m2): return "number of cols <matrix1> must be equal to number of rows of <matrix2>"
         multiplied = zeros(len(m1), len(m2[0]))
         for rows in range(len(m1)):
             for cols in range(len(m2[0])):
               for i in range(len(m1[0])):
                   multiplied[rows][cols] += m1[rows][i] * m2[i][cols]
         return multiplied
    else: return []

   
def subtract(m1, m2):
    """Subtract two matrix."""
    if typeOf(m1)==1 and typeOf(m2)==1: #Matrix - Matrix
       return add(m1, oppose(m2))
    elif typeOf(m1)==0 and typeOf(m2)==0: #Array - Array
         return add(m1, oppose(m2))
    return "The <object> isn't an array or a matrix"

"""
def generateWeights(nrows, ncols):
    result = []
    for rows in range(nrows):
        line = [0]*ncols
        result.append(line)
    return result

def generateBiasWeights(numberHiddenLayers):
    biasMatrix = []
    for rows in range(numberHiddenLayers):
        line = [0]*1
        biasMatrix.append(line)
    return biasMatrix
"""
def generateBias(numberHiddenLayers):
    biasMatrix = []
    for rows in range(numberHiddenLayers):
        line = [1]*1
        biasMatrix.append(line)
    return biasMatrix

def generateWeights(nrows, ncols):
    result = []
    for rows in range(nrows):
        line = [random.random()]*ncols
        result.append(line)
    return result

def generateBiasWeights(numberHiddenLayers):
    biasMatrix = []
    for rows in range(numberHiddenLayers):
        line = [random.random()]*1
        biasMatrix.append(line)
    return biasMatrix



