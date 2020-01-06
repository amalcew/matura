# 145
# 468
file = open("data/80/dane_trojkaty.txt")
triangles = file.readlines()
triangles = list(map(int, triangles))
# last number - 5573


def zad1():
    print("80.1")
    for x in range(0, len(triangles)-2):
        tmp = [triangles[x], triangles[x+1], triangles[x+2]]
        c = max(tmp)
        tmp.remove(max(tmp))
        a = tmp[0]
        b = tmp[1]
        if a**2 + b**2 == c**2:
            print(str(a)+", "+str(b)+", "+str(c))
    print()


def zad2():
    print("80.2")
    answer = []
    for x in range(len(triangles)):
        a = triangles[x]
        for y in range(len(triangles)):
            b = triangles[y]
            for z in range(len(triangles)):
                c = triangles[z]
                if a != b and b != c and a != c:
                    tmp = [a, b, c]
                    mx = max(tmp)
                    tmp.remove(max(tmp))
                    if tmp[0] + tmp[1] > mx:
                        answer.append(a+b+c)
    print(max(answer))
    print()


def zad3():
    tr = []
    for x in range(len(triangles)):
        a = triangles[x]
        for y in range(len(triangles)):
            b = triangles[y]
            for z in range(len(triangles)):
                c = triangles[z]
                if a != b and b != c and a != c:
                    tmp = [a, b, c]
                    mx = max(tmp)
                    tmp.remove(max(tmp))
                    if tmp[0] + tmp[1] > mx:
                        tmp = [a, b, c]
                        triangle = sorted(tmp)
                        if triangle not in tr:
                            tr.append(triangle)
                            print(len(tr))
    print()
    print(len(tr))



def test():
    pass

# zad1()
# zad2()
zad3()
# test()
