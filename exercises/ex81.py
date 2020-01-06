from math import sqrt
# 146 468
file = open("data/81/wspolrzedne.txt")
file = file.readlines()
w = []
for line in file:
    tmp = list(map(int, line.split()))
    a = {"x": tmp[0], "y": tmp[1]}
    b = {"x": tmp[2], "y": tmp[3]}
    c = {"x": tmp[4], "y": tmp[5]}
    l = {"a": a, "b": b, "c": c}
    w.append(l)

file_tr = open("data/81/wspolrzedneTR.txt")
file_tr = file_tr.readlines()
w_tr = []
for line in file_tr:
    tmp = list(map(int, line.split()))
    a = {"x": tmp[0], "y": tmp[1]}
    b = {"x": tmp[2], "y": tmp[3]}
    c = {"x": tmp[4], "y": tmp[5]}
    l = {"a": a, "b": b, "c": c}
    w_tr.append(l)


def z1():
    k = 0
    for x in range(len(w)):
        line = w[x]
        if line["a"]["x"] > 0 and line["a"]["y"] > 0 and line["b"]["x"] > 0 and line["b"]["y"] > 0 and line["c"]["x"] \
                > 0 and line["c"]["y"] > 0:
            k += 1
    print("81.1 - "+str(k))
    print()


def z2():
    k = 0
    for x in range(len(w)):
        try:
            if w[x]["c"]["y"] == round((w[x]["b"]["y"] - w[x]["a"]["y"])/(w[x]["b"]["x"] - w[x]["a"]["x"]) *
                                       w[x]["c"]["x"] + w[x]["a"]["y"] - (w[x]["b"]["y"] - w[x]["a"]["y"])/
                                       (w[x]["b"]["x"] - w[x]["a"]["x"]) * w[x]["a"]["x"], 1):
                k += 1
        except ZeroDivisionError:
            if w[x]["c"]["x"] == w[x]["a"]["x"]:
                k += 1
    print("81.2 - "+str(k))
    print()


def z3():
    k = 0
    tr = {}
    for x in range(len(w_tr)):
        s1 = sqrt((w_tr[x]["b"]["x"] - w_tr[x]["a"]["x"])**2 + (w_tr[x]["b"]["y"] - w_tr[x]["a"]["y"])**2)
        s2 = sqrt((w_tr[x]["c"]["x"] - w_tr[x]["a"]["x"]) ** 2 + (w_tr[x]["c"]["y"] - w_tr[x]["a"]["y"]) ** 2)
        s3 = sqrt((w_tr[x]["b"]["x"] - w_tr[x]["c"]["x"]) ** 2 + (w_tr[x]["b"]["y"] - w_tr[x]["c"]["y"]) ** 2)
        if s1 + s2 + s3 > k:
            k = s1 + s2 + s3
            tr = w_tr[x]
    print("81.3 - "+str(tr)+", "+str(round(k, 2)))
    print()


def z4():
    k = 0
    for x in range(len(w_tr)):
        s1 = sqrt((w_tr[x]["b"]["x"] - w_tr[x]["a"]["x"]) ** 2 + (w_tr[x]["b"]["y"] - w_tr[x]["a"]["y"]) ** 2)
        s2 = sqrt((w_tr[x]["c"]["x"] - w_tr[x]["a"]["x"]) ** 2 + (w_tr[x]["c"]["y"] - w_tr[x]["a"]["y"]) ** 2)
        s3 = sqrt((w_tr[x]["b"]["x"] - w_tr[x]["c"]["x"]) ** 2 + (w_tr[x]["b"]["y"] - w_tr[x]["c"]["y"]) ** 2)
        s = [s1, s2, s3]
        m_s = max(s)
        s.remove(max(s))
        if round(m_s**2, 2) == round(s[0]**2 + s[1]**2, 2):
            k += 1
    print("81.4 - "+str(k))
    print()


def z5():
    print("81.5: ")
    for x in range(len(w_tr)):
        d = {"x": w_tr[x]["c"]["x"] - (w_tr[x]["b"]["x"] - w_tr[x]["a"]["x"]), "y": w_tr[x]["c"]["y"] - (w_tr[x]["b"]["y"] - w_tr[x]["a"]["y"])}
        if d["x"] == d["y"]:
            tr = w_tr[x]
            tr["d"] = d
            print(tr)


z1()
z2()
z3()
z4()
z5()