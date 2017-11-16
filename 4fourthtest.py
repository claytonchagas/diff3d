# stl_file1 = '/home/clayton/cuboasc.stl'
stl_file1 = '/home/clayton/Vídeos/cilindroconefinalascii2.stl'
# stl_file1 = '/home/clayton/Vídeos/cilindrofreecadfinalascii2.stl'
f1 = open(stl_file1, 'r')
data1 = f1.readlines()
print(len(data1))
i = 0
j = 0
k = 0
m = 0
n = 0
r = []
r1 = []
r2 = []
for x in range(len(data1)):
    if x == (7 * i) + 3 or x == (7 * i) + 4 or x == (7 * i) + 5:
        print(i)
        print(data1[x])
        t = data1[x]
        t2 = t.split()
        print(t2)
        j += 1
        if j > 2:
            k += 1
            j = 0
            i += 1
        print(t2[1], t2[2], t2[3])
        r.append([t2[1], t2[2], t2[3]])
        n += 1
        print(r)
for y in range((int((len(data1)-2)/7))*3):
    for z in range(0, 3):
        print(r[y][z])
        r1.append(r[y][z])
        m += 1
        print(m)
    print(r1)
    # r2.append(r1)
    # print(r2)
    if m == 9:
        r2.append([r1[0], r1[1], r1[2], r1[3], r1[4], r1[5], r1[6], r1[7], r1[8]])
        r1.clear()
        m = 0
# print(m)
print(r2)
f1.close()

# stl_file2 = '/home/clayton/cuboasc2.stl'
stl_file2 = '/home/clayton/Vídeos/cilindrofreecadfinalascii2.stl'
# stl_file2 = '/home/clayton/Vídeos/cilindroconefinalascii2copy.stl'
# stl_file2 = '/home/clayton/Vídeos/cilindroconefinalascii2.stl'
f2 = open(stl_file2, 'r')
data2 = f2.readlines()
print(len(data2))
i = 0
j = 0
k = 0
m = 0
n = 0
rc = []
r3 = []
r4 = []
for x in range(len(data2)):
    if x == (7 * i) + 3 or x == (7 * i) + 4 or x == (7 * i) + 5:
        print(i)
        print(data2[x])
        t = data2[x]
        t2 = t.split()
        print(t2)
        j += 1
        if j > 2:
            k += 1
            j = 0
            i += 1
        print(t2[1], t2[2], t2[3])
        rc.append([t2[1], t2[2], t2[3]])
        n += 1
        print(rc)
for y in range((int((len(data2)-2)/7))*3):
    for z in range(0, 3):
        print(rc[y][z])
        r3.append(rc[y][z])
        m += 1
        print(m)
    print(r3)
    # r2.append(r1)
    # print(r2)
    if m == 9:
        r4.append([r3[0], r3[1], r3[2], r3[3], r3[4], r3[5], r3[6], r3[7], r3[8]])
        r3.clear()
        m = 0
# print(m)
print(r4)
f2.close()
q = r4[0]
print(q[0])
# result = (r == rc)
# print(result)
print("r4: ", r4)
print("r2: ", r2)
diff = []


def out():
    # for w in range((int((len(data2)-2)/7))):
    for k in range((int((len(data1)-2)/7))):
        if r4[w] == r2[k]:
            return
        # else:
    diff.append(r4[w])
#     if r4[w] == r2[w]:
#         print()
for w in range((int((len(data2)-2)/7))):
    out()


def out2():
    # for w in range((int((len(data2)-2)/7))):
    for k in range((int((len(data2)-2)/7))):
        if r2[w] == r4[k]:
            return
        # else:
    diff.append(r2[w])
#     if r4[w] == r2[w]:
#         print()
for w in range((int((len(data1)-2)/7))):
    out2()


if len(diff) == 0:
    print("São iguaizinhos, nada mudou!")
else:
    print("Foi encontrada a seguinte diferença malhas triangulares entre os dois modelos: ", diff)
    print("Foi encontrada a seguinte quantidade de poligonos diferentes: ", len(diff))

