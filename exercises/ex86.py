file = open("data/86/dane_wybory.txt")
file = file.readlines()
os = []
for line in file:
    os.append(line.strip())


def wk(gk, mk):
    return gk/(2*mk + 1)


def ex86_3():
    print("zad 3")
    for x in range(len(os)):
        tmp = os[x].split()
        o = tmp[0]
        k = [{"k": "k1", "gk": int(tmp[1]), "mk": 0},
             {"k": "k2", "gk": int(tmp[2]), "mk": 0},
             {"k": "k3", "gk": int(tmp[3]), "mk": 0},
             {"k": "k4", "gk": int(tmp[4]), "mk": 0},
             {"k": "k5", "gk": int(tmp[5]), "mk": 0}]

        for y in range(0, 20):
            w1 = wk(k[0]["gk"], k[0]["mk"])
            w2 = wk(k[1]["gk"], k[1]["mk"])
            w3 = wk(k[2]["gk"], k[2]["mk"])
            w4 = wk(k[3]["gk"], k[3]["mk"])
            w5 = wk(k[4]["gk"], k[4]["mk"])
            w = [w1, w2, w3, w4, w5]
            w_max = max(w)
            if w_max == w1:
                m = k[0]["mk"] + 1
                k[0]["mk"] = m
            if w_max == w2:
                m = k[1]["mk"] + 1
                k[1]["mk"] = m
            if w_max == w3:
                m = k[2]["mk"] + 1
                k[2]["mk"] = m
            if w_max == w4:
                m = k[3]["mk"] + 1
                k[3]["mk"] = m
            if w_max == w5:
                m = k[4]["mk"] + 1
                k[4]["mk"] = m

        print(o+" "+str(k[0]["mk"])+" "+str(k[1]["mk"])+" "+str(k[2]["mk"])+" "+str(k[3]["mk"])+" "+str(k[4]["mk"]))
    print()


def ex86_4():
    print("zad 4")
    b = open("data/86/regiony.txt")
    b = b.readlines()
    rs = []
    for line in b:
        rs.append(line)

    for x in range(len(rs)):
        tmp = rs[x].split()
        o = tmp[0]
        k = [{"k": "k1", "gk": int(tmp[1]), "mk": 0},
             {"k": "k2", "gk": int(tmp[2]), "mk": 0},
             {"k": "k3", "gk": int(tmp[3]), "mk": 0},
             {"k": "k4", "gk": int(tmp[4]), "mk": 0},
             {"k": "k5", "gk": int(tmp[5]), "mk": 0}]
        for y in range(0, 100):
            w1 = wk(k[0]["gk"], k[0]["mk"])
            w2 = wk(k[1]["gk"], k[1]["mk"])
            w3 = wk(k[2]["gk"], k[2]["mk"])
            w4 = wk(k[3]["gk"], k[3]["mk"])
            w5 = wk(k[4]["gk"], k[4]["mk"])
            w = [w1, w2, w3, w4, w5]
            w_max = max(w)
            if w_max == w1:
                m = k[0]["mk"] + 1
                k[0]["mk"] = m
            if w_max == w2:
                m = k[1]["mk"] + 1
                k[1]["mk"] = m
            if w_max == w3:
                m = k[2]["mk"] + 1
                k[2]["mk"] = m
            if w_max == w4:
                m = k[3]["mk"] + 1
                k[3]["mk"] = m
            if w_max == w5:
                m = k[4]["mk"] + 1
                k[4]["mk"] = m

        print(o+" "+str(k[0]["mk"])+" "+str(k[1]["mk"])+" "+str(k[2]["mk"])+" "+str(k[3]["mk"])+" "+str(k[4]["mk"]))
    print()


def ex86_5():
    print("zad 5")
    m1 = 10
    m2 = 20
    m3 = 50
    for i in range(0, 100000):
        k = [{"k": "q", "gk": i, "mk": 0}, {"k": "r", "gk": 100000-i, "mk": 0}]
        for x in range(0, 2*m1):
            w1 = wk(k[0]["gk"], k[0]["mk"])
            w2 = wk(k[1]["gk"], k[1]["mk"])
            if w1 > w2:
                m = k[0]["mk"] + 1
                k[0]["mk"] = m
            else:
                m = k[1]["mk"] + 1
                k[1]["mk"] = m
        if k[0]["mk"] == m1:
            print("m1 - "+str(k[0]["gk"]-1))
            break

    for i in range(0, 100000):
        k = [{"k": "q", "gk": i, "mk": 0}, {"k": "r", "gk": 100000-i, "mk": 0}]
        for x in range(0, 2*m2):
            w1 = wk(k[0]["gk"], k[0]["mk"])
            w2 = wk(k[1]["gk"], k[1]["mk"])
            if w1 > w2:
                m = k[0]["mk"] + 1
                k[0]["mk"] = m
            else:
                m = k[1]["mk"] + 1
                k[1]["mk"] = m
        if k[0]["mk"] == m2:
            print("m2 - "+str(k[0]["gk"]-1))
            break

    for i in range(0, 100000):
        k = [{"k": "q", "gk": i, "mk": 0}, {"k": "r", "gk": 100000-i, "mk": 0}]
        for x in range(0, 2*m3):
            w1 = wk(k[0]["gk"], k[0]["mk"])
            w2 = wk(k[1]["gk"], k[1]["mk"])
            if w1 > w2:
                m = k[0]["mk"] + 1
                k[0]["mk"] = m
            else:
                m = k[1]["mk"] + 1
                k[1]["mk"] = m
        if k[0]["mk"] == m3:
            print("m3 - "+str(k[0]["gk"]-1))
            break


ex86_3()
ex86_4()
ex86_5()