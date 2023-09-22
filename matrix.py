def transpose(matrix):
    if len(matrix) == 0:
        return []
    result = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(0)
        result.append(row)

#  result = []
    for i in range(len(matrix)):
       # row = []
        for j in range(len(matrix[i])):
           result[j][i] = matrix[i][j]
         # row.append()
       # result.append(row)
    
    return result
# print(transpose([[1,2],[3,4],[5,6]]))          


def powers(list,a,b):
    powersMatrix = []
    for i in range(len(list)):
        row = []
        for n in range(a,b+1):
          new_value = list[i]**n
          row.append(new_value)
        powersMatrix.append(row)
    return powersMatrix

print(powers([2,3,4],1,3))

def matmul(N,M):
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

def invert(A):
    if len(A) == 2:
        det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    
    return [[A[1][1]/det, -1*A[0][1]/det],
            [-1*A[1][0]/det, A[0][0]/det]]


def loadtxt(file):
    filename = open(file)
    text = filename.readlines()
    values = []
    for row in text:
        row = row.split()
        data = []
        for r in row:
            data.append(float(r))
        values.append(data)
    return values




