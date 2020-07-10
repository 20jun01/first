import sys
import math
import pandas as pd
import numpy as np

num = 0
data1 = []
data2 = []
with open(sys.argv[1]) as fp:
    num = int(fp.readline())
    for i in range(num):
        line = fp.readline()
        s = line.split()
        data1.append(float(s[0]))
        data2.append(float(s[1]))

s1 = pd.Series(data1)
s2 = pd.Series(data2)
print(s1.corr(s2))