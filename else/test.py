# 引数を使用するためのライブラリ
import sys

# 個数とデータ本体の初期化
num = 0
data = []

# ファイルからのデータ読み込み
with open(sys.argv[1]) as fp:
  num = int(fp.readline())
  for i in range(num):
    line = fp.readline()
    s = line.split()
    data.append([float(s[0]), float(s[1])])

# 平均値を求める関数
def average():
  total = [0, 0]
  for i in range(num):
    total[0] = total[0] + data[i][0]
    total[1] = total[1] + data[i][1]
  avex = total[0] / num
  avey = total[1] / num
  return([avex, avey])

ave = average()
print("avex = ", ave[0])
print("avey = ", ave[1])