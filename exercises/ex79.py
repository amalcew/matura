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
    for x in range(len(circles)):
        master = circles[x]
        for y in range(len(circles)):
            slave = circles[y]
            if master is not slave:
                if master["r"] == slave["r"]:
                    pass


# ex79_1()
ex79_2()