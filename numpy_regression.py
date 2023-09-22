from numpy import *
import sys
import matplotlib.pyplot as plt


def powers(list,a,b):
    powersMatrix = []
    for i in range(len(list)):
        row = []
        for n in range(a,b+1):
          new_value = list[i]**n
          row.append(new_value)
        powersMatrix.append(row)
    return array(powersMatrix)

def poly(a,x):
    Y = 0
    for i in range(len(a)):
        Y = Y + (a[i]*(x**i))
    return Y


def main():
    data = loadtxt(sys.argv[1])

    n = int(sys.argv[2])

    extract_data = transpose(data)

    X = extract_data[0] 
    Y = extract_data[1]


    Xp = powers(X,0,n)
    Yp = powers(Y,1,1)
    Xpt = Xp.transpose()

    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0]

    X2 = linspace(X[0],X[-1],(X[-1] - X[0])/0.2).tolist()
    
    Y2 = (poly(a,X2))
    
    # for i in range(len(X)):
    #      Y2.append(a*X[i])


    plt.plot(X,Y,'ro')
    plt.plot(X2,Y2)
    plt.show()
    # print(X[1])
    # print(Y2)

main()