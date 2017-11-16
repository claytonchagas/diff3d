# import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

stl_file = '/home/clayton/cuboasc.stl'
# stl_file = '/home/clayton/Documentos/3D_Diff/models/modelos_cascavel/cascavelasc.stl'
# stl_file = '/home/clayton/Documentos/3D_Diff/models/esfera.stl'
# stl_file = '/home/clayton/Documentos/3D_Diff/models/f16.stl'
tmp_file = '/home/clayton/tmp_cuboasc.stl'
# tmp_file = '/home/clayton/Documentos/3D_Diff/models/modelos_cascavel/tmp_cascavelasc.stl'
# tmp_file = '/home/clayton/Documentos/3D_Diff/models/tmp_esfera.stl'
# tmp_file = '/home/clayton/Documentos/3D_Diff/models/tmp_f16.stl'
tmp_file2 = '/home/clayton/tmp_cuboasc2.stl'
# tmp_file2 = '/home/clayton/Documentos/3D_Diff/models/modelos_cascavel/tmp_cascavelasc2.stl'
# tmp_file2 = '/home/clayton/Documentos/3D_Diff/models/tmp_esfera2.stl'
# tmp_file2 = '/home/clayton/Documentos/3D_Diff/models/tmp_f162.stl'
f = open(stl_file, 'r')
o = open(tmp_file, 'w')
# o2 = open(tmp_file2, 'w')
data = f.readlines()
i = 0
j = 0
k = 0
fig1 = plt.figure()
ax = Axes3D(fig1)
print(data[1])
r1 = []
for x in range(len(data)):
    # for line in data:
    #     if i == 3 or i == 4 or i == 5:
    if x == (7*i)+3 or x == (7*i)+4 or x == (7*i)+5:
        # print(k)
        # print(data[x])
        t = data[x]
        t2 = t.split()
        print(t2[1], t2[2], t2[3])
        o.write(data[x])
        r = t2[1], t2[2], t2[3]
        r1.append(r)
        # o2.write(t2)
        j += 1
        if j > 2:
            k += 1
            j = 0
            i += 1
        # print(line)
        # i += 1
    # x += 7
# for line in f:
# print(f.readline())
# for line in f.readlines():
#     # if line.index()
#     print(line)
# data = np.genfromtxt(f, delimiter=',')
print(r1)
print(r1[0])
print(r1[0][1])
# Xa = [float(r1[0][0]), float(r1[1][0]), float(r1[2][0]), float(r1[0][0])]
# Ya = [float(r1[0][1]), float(r1[1][1]), float(r1[2][1]), float(r1[0][1])]
# Za = [float(r1[0][2]), float(r1[1][2]), float(r1[2][2]), float(r1[0][2])]
# print(Xa)
print(int(len(r1))/3)
# ax.plot3D(Xa, Ya, Za)
f.close()
o.close()
# plt.show()
# n = 0
# for m in range(int(len(r1)/3)):
    # Xa = [float(r1[n][0]), float(r1[n+1][0]), float(r1[n+2][0]), float(r1[n][0])]
    # Xa = [r1[n][0], r1[n + 1][0], r1[n + 2][0], r1[n][0]]
    # Ya = [float(r1[n][1]), float(r1[n+1][1]), float(r1[n+2][1]), float(r1[n][1])]
    # Ya = [r1[n][1], r1[n + 1][1], r1[n + 2][1], r1[n][1]]
    # Za = [float(r1[n][2]), float(r1[n+1][2]), float(r1[n+2][2]), float(r1[n][2])]
    # Za = [r1[n][2], r1[n + 1][2], r1[n + 2][2], r1[n][2]]
    # ax.plot3D(Xa, Ya, Za)
    # n += 3
    # print(n)
# plt.show()
# plt.close()
# o2.write()
