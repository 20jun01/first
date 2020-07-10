import sys

num = 0
data = []

with open(sys.argv[1]) as fp:
    num = int(fp.readline())
    for i in range(num):
        line = fp.readline()
        s = line.split()
        data.append([float(s[0]),float(s[1])])

def square(x):
    return x*x

def average(x):
    ave = 0
    for i in range(len(x)):
        ave += x[i]
    return ave/len(x)

def average2(x):
    ave = [0,0]
    for i in range(len(x)):
        ave[0] += x[i][0]
        ave[1] += x[i][1]
    return ave[0]/len(x),ave[1]/len(x)

def app(data):
    sigma_xy = 0
    sigma_x2 = 0
    sigma_x = 0
    sigma_y = 0
    # ns_xsy = 0
    # ns_x2sy = 0
    # ns_xysx = 0
    for i in range(len(data)):
        sigma_xy += data[i][0] * data[i][1]
        sigma_x2 += square(data[i][0])
        sigma_x += data[i][0]
        sigma_y += data[i][1]
    # for i in range(len(data)):
    #     ns_xsy += data[i][0]*sigma_y
    #     ns_x2sy += data[i][0]*data[i][0]*sigma_y
    #     ns_xysx += data[i][0]*data[i][1]*sigma_x
    a = (len(data)*sigma_xy - sigma_x * sigma_y) / (len(data) * sigma_x2 - square(sigma_x))
    b = (sigma_x2 * sigma_y - sigma_xy * sigma_x) / (len(data) * sigma_x2 - square(sigma_x))
    # a = ((num*sigma_xy) - ns_xsy)/((num*sigma_x2)-(sigma_x*sigma_x))
    # b = (ns_x2sy - ns_xysx)/((num*sigma_x2) - (sigma_x*sigma_x))
    return a,b

def culR(data,a,b):
    child = 0
    mam = 0
    _,ave_y = average2(data)
    for i in range(len(data)):
        child += square(data[i][1] - (a*data[i][0] + b))
        mam += square(data[i][1] - ave_y)
    
    return 1-(child/mam)

a,b = app(data)
print("y = {:.3f}x + {:.3f}".format(a,b))
R2 = culR(data,a,b)
print("R2:{}".format(R2))