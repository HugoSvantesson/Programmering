def transpose(matrix):
#Detta funkar   
    tpRows = len(matrix[0])   #The transposed rows length is equal to the first matrix's columns
    tpColumns = len(matrix)   #Same for the columns but to the first matrix's rows
    transposedMatrix = [(tpColumns*[0]) for i in range(tpRows)]    #Creates an empty "Matrix"
  #  result = []
    for i in range(len(matrix)):
       # row = []
        for j in range(len(matrix[i])):
           transposedMatrix[j][i] = matrix[i][j]
         # row.append()
       # result.append(row)
    
    return transposedMatrix

# print(transpose([[1,2],[3,4],[5,6]]))          

#Detta funkar
   # transposedMatrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]  
   #  return transposedMatrix
 
#Detta funkar
    # for i in range(len(matrix[0])):
    #    row = []
    #    for newlist in matrix:
    #        row.append(newlist[i])
    #    transposedlist.append(row)
    # return transposedlist

def powers(list,a,b):
    powersMatrix = []
    for i in range(len(list)):
        row = []
        for n in range(a,b+1):
          new_value = list[i]**n
          row.append(new_value)
        #row.append(list[i]** n for n in range(a,b+1))
        powersMatrix.append(row)
    return powersMatrix

# print(powers([2,3,4],1,3))

def matmul(N,M):
    # MultRows = len(N)   #The transposed rows length is equal to the first matrix's columns
    # MultColumns = len(M[0])   #Same for the columns but to the first matrix's rows
    # MultMatrix = [(MultColumns*[0]) for i in range(MultRows)]     #Creates an empty "Matrix"
    result = []
    for i in range(len(N)):
        row = []
        for j in range(len(M[0])):
            row.append(0)
        result.append(row)

    for i in range(len(N)):
        for j in range(len(M[0])):
            for k in range(len(M)):
                result[i][j] += N[i][k] * M[k][j]
    
    return result

# print(matmul([[1,2,3],[4,5,6]],[[7,8,9,10],[11,12,13,14],[15,16,17,18]]))

def invert(A):
    if len(A) == 2:
        det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    
    return [[A[1][1]/det, -1*A[0][1]/det],
            [-1*A[1][0]/det, A[0][0]/det]]
