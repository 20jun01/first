import sys
import math

num = 0
data = []

with open(sys.argv[1]) as fp:
    num = int(fp.readline())
    for i in range(num):
        line = fp.readline()
        s = line.split()
        data.append([float(s[0]),float(s[1])])

def average(data):
    total = [0,0]
    for i in range(num):
        total[0] = total[0] + data[i][0]
        total[1] = total[1] + data[i][1]
        avex = total[0]/num
        avey = total[1]/num
    return ([avex,avey])

def cul_sig(data,ave):
    sigs = [[],[]]
    for i in range(len(data)):
        sigs[0].append(ave[0] - data[i][0])
        sigs[1].append(ave[1] - data[i][1])
    return sigs

def square(x):
    return x*x

def St(sig):
    temp = map(square,sig)
    t=sum(temp)
    return math.sqrt(t/len(sig))

def cor(sigs):
    C = 0
    for i in range(len(sigs[0])):
        C += sigs[0][i]*sigs[1][i]
    return C/len(sigs[0])

def culR(data):
    ave = average(data)
    sig = cul_sig(data,ave)
    Sx = St(sig[0])
    Sy = St(sig[1])
    Cx_y =  cor(sig)
    return Cx_y/(Sx*Sy)

print(culR(data))
