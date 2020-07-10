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


def culR(a,b,x,y):
    child = np.array(list(map(square,y-(a*x+b)))).sum()
    mam = np.array(list(map(square,y-y.mean()))).sum()
    return 1-(child/mam)

def approximation(x,y,N):
    y_sum = y.sum()
    x_sum = x.sum()
    x_sq = np.matmul(x,x)
    a_child = N * np.matmul(x,y) - (x_sum*y_sum)
    b_child = np.matmul(x,x) * y_sum - np.matmul(x,y) * x_sum
    mam = N * x_sq - square(x_sum)
    a = a_child/mam
    # b = (y_sum-a*x_sum)/N
    b = b_child/mam
    return a,b

a,b = approximation(data_x,data_y,num)
print("y = {:.3f}x + {:.3f}".format(a,b))
R = culR(a,b,data_x,data_y)
print("R:{}".format(R))

x = np.arange(100)
plt.plot(x,a*x + b,color = "r")
plt.scatter(data_x[:100],data_y[:100])
# plt.scatter(data_x,data_y)
plt.show()

# x_std = np.sqrt(np.matmul(data_x - data_x.mean(),data_x - data_x.mean())/num)
# y_std = np.sqrt(np.matmul(data_y - data_y.mean(),data_y - data_y.mean())/num)
# C_xy = np.matmul(data_x-data_x.mean(),data_y - data_y.mean())/num
# R2 = C_xy/(x_std*y_std)
# print(R2)