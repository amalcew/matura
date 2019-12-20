from math import sqrt
file = open("data/79/okregi.txt")
file = file.readlines()
circles = []
for x in range(len(file)):
    circle = {}
    tmp = file[x].split()
    tmp = list(map(float, tmp))
    circle["x"], circle["y"], circle["r"] = tmp[0], tmp[1], tmp[2]
    circles.append(circle)


def ex79_1():
    print("ex79.1")
    i = 0
    ii = 0
    iii = 0
    iv = 0
    n = 0
    for j in range(len(circles)):
        x = circles[j]["x"]
        y = circles[j]["y"]
        r = circles[j]["r"]
        if x > 0:
            if y > 0:
                if r <= abs(x) and r <= abs(y):
                    i += 1
                else:
                    n += 1
            elif y < 0:
                if r <= abs(x) and r <= abs(y):
                    iv += 1
                else:
                    n += 1
        elif x < 0:
            if y > 0:
                if r <= abs(x) and r <= abs(y):
                    ii += 1
                else:
                    n += 1
            elif y < 0:
                if r <= abs(x) and r <= abs(y):
                    iii += 1
                else:
                    n += 1
        else:
            n += 1
    print(i)
    print(ii)
    print(iii)
    print(iv)
    print(n)
    print()


def ex79_2():
    print("ex79.2")
    mirror_circles = []
    for x in range(len(circles)):
        master = circles[x]
        for y in range(len(circles)):
            slave = circles[y]
            if master is not slave:
                if master["r"] == slave["r"]:
                    if master["y"] == slave["y"] and abs(master["x"]) == abs(slave["x"]):
                        tmp = [master, slave]
                        rev_tmp = [slave, master]
                        if tmp not in mirror_circles and rev_tmp not in mirror_circles:
                            mirror_circles.append(tmp)

                    if master["x"] == slave["x"] and abs(master["y"]) == abs(slave["y"]):
                        tmp = [master, slave]
                        rev_tmp = [slave, master]
                        if tmp not in mirror_circles and rev_tmp not in mirror_circles:
                            mirror_circles.append(tmp)

    print(len(mirror_circles))
    print()


def ex79_3():
    print("ex79.3")
    perpendicular_circles = []
    for x in range(len(circles)):
        master = circles[x]
        for y in range(len(circles)):
            slave = circles[y]
            if master is not slave:
                if master["r"] == slave["r"]:
                    if master["x"] == slave["y"] and abs(master["y"]) == slave["x"]:
                        tmp = [master, slave]
                        rev_tmp = [slave, master]
                        if tmp not in perpendicular_circles and rev_tmp not in perpendicular_circles:
                            perpendicular_circles.append(tmp)

                    if master["x"] == abs(slave["y"]) and master["y"] == slave["x"]:
                        tmp = [master, slave]
                        rev_tmp = [slave, master]
                        if tmp not in perpendicular_circles and rev_tmp not in perpendicular_circles:
                            perpendicular_circles.append(tmp)

                    if abs(master["x"]) == slave["y"] and master["y"] == slave["x"]:
                        tmp = [master, slave]
                        rev_tmp = [slave, master]
                        if tmp not in perpendicular_circles and rev_tmp not in perpendicular_circles:
                            perpendicular_circles.append(tmp)

    print(len(perpendicular_circles))
    print()


def ex79_4():
    print("ex79_4")
    chain_length = []
    k = 1
    for i in range(1, len(circles)):
        master = circles[i]
        slave = circles[i-1]
        dis = sqrt((master["x"] - slave["x"])**2 + (master["y"] - slave["y"])**2)
        if dis > master["r"] + slave["r"] or dis < abs(master["r"] - slave["r"]):
            chain_length.append(k)
            k = 1
        else:
            k += 1

    for x in range(len(chain_length)):
        if chain_length[x] > 2:
            print(chain_length[x])
    print()
    print("Max: " + str(max(chain_length)))


ex79_1()
ex79_2()
ex79_3()
ex79_4()
