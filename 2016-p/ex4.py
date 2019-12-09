from math import sqrt

file = open("dane/dane.txt")
file = file.readlines()
circles = []

for x in range(len(file)):
    circle = {"x": 0, "y": 0, "r": 0}
    line = file[x].split()
    line = list(map(int, line))
    circle["x"] = line[0]
    circle["y"] = line[1]
    circle["r"] = line[2]
    circles.append(circle)


def ex4_1():
    k = 0
    for x in range(len(circles)):
        if circles[x]["r"] == 1:
            k += 1
            print(circles[x])
    print(k)


def ex4_2():
    tmp = []
    for x in range(len(circles)):
        k = 0
        for y in range(len(circles)):
            if circles[x] is not circles[y]:
                distance = sqrt((circles[x]["x"] - circles[y]["x"])**2 + (circles[x]["y"] - circles[y]["y"])**2)
                if distance <= circles[x]["r"]:
                    k += 1
        circles[x]["agario"] = k

    for x in range(len(circles)):
        tmp.append(circles[x]["agario"])
    print(circles[tmp.index(max(tmp))])


def ex4_3():
    k = 0
    tmp = []
    for x in range(len(circles)):
        for y in range(len(circles)):
            if circles[x] is not circles[y]:
                distance = sqrt((circles[x]["x"] - circles[y]["x"]) ** 2 + (circles[x]["y"] - circles[y]["y"]) ** 2)
                if distance == circles[x]["r"] + circles[y]["r"] or \
                        distance == abs(circles[x]["r"] - circles[y]["r"]):
                    k += 1
                    tmp.append(str(circles[x]["x"])+" "+str(circles[x]["y"])+" "+str(circles[x]["r"])+" "
                               + str(circles[y]["x"])+" "+str(circles[y]["y"])+" "+str(circles[y]["r"]))

    print(k)
    for x in range(len(tmp)):
        print(tmp[x])
