import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

num = 0
data = []

with open(sys.argv[1]) as fp:
    num = int(fp.readline())
    for i in range(num):
        line = fp.readline()
        s = line.split()
        data.append([float(s[0]),float(s[1])])
data = np.array(data)
data_x = data[:,0]
data_y = data[:,1]

def square(x):
    return x*x


def culR(a2,a1,a0,x,y):
    child = np.array(list(map(square,y-(a2*x*x + a1*x +a0)))).sum()
    mam = np.array(list(map(square,y-y.mean()))).sum()
    return 1-(child/mam)

def approximation(x,y,N):
    Y = y.sum()
    X = x.sum()
    x_sq = np.array(list(map(square,x)))
    XY = np.matmul(x,y)
    X2Y = np.matmul(x*x,y)
    X2 = np.matmul(x,x)
    X3 = np.matmul(x*x,x)
    X4 = np.matmul(x*x,x*x)
    A = 2*X * X2 * X3 + N * X2 * X4 - X*X * X4 - N * X3*X3 - X2*X2*X2
    child_a0 = -X2*X2 * X2Y + X * X3 * X2Y - X * X4 * XY + X2 * X3 * XY - X3*X3 * Y + X2 * X4 * Y
    child_a1 = X * X2 * X2Y - N * X3 * X2Y + N * X4 * XY - X2*X2 * XY + X2 * X3 * Y - X * X4 * Y
    child_a2 = (N * X2 * X2Y) - (X*X * X2Y) + (X * X2 * XY) - (N * X3 * XY) + (X * X3 * Y) - (X2*X2 * Y)
    a0 = child_a0 / A
    a1 = child_a1 / A
    a2 = child_a2 / A
    return a0,a1,a2

a0,a1,a2 = approximation(data_x,data_y,num)
print("y = {:.3f}x^2 + {:.3f}x + {:.3f}".format(a2,a1,a0))
R = culR(a2,a1,a0,data_x,data_y)
print("R2:{}".format(R))
x = np.arange(100)
plt.plot(x,a2*x*x + a1*x + a0,color = "r")
plt.scatter(data_x[:100],data_y[:100])
# plt.scatter(data_x,data_y)
plt.show()
