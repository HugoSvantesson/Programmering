from matrix import *
import sys
import matplotlib.pyplot as plt

def main():
    data = loadtxt(sys.argv[1])
    # Xlist = []
    # Ylist = []

    extract_data = transpose(data)

    X = extract_data[0] 
    Y = extract_data[1]

    Xp = powers(X,0,1)
    Yp = powers(Y,1,1)
    Xpt = transpose(Xp)

    [[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

    Y2 = []
    for i in range(len(X)):
        Y2.append(b+m*X[i])

    plt.plot(X,Y,'ro')
    plt.plot(X,Y2)
    plt.show()
    # print(extract_data)

main()



    