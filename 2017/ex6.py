# TODO ex6_3 - poprawić pętlę sprawdzającą kontrastowość pikseli
def ex6_1():
    data = open("data/dane.txt", "r")
    check_min = 255
    check_max = 0
    for x in range(0, 200):
        row = data.readline()
        row_list = row.split()
        for y in range(0, 320):
            value = int(row_list[y])
            if value < check_min:
                check_min = value
            if value > check_max:
                check_max = value
    print("Najniższa wartość piksela: "+str(check_min))
    print("Najniższa wartość piksela: "+str(check_max))
    data.close()


def ex6_2():
    data = open("data/dane.txt", "r")
    result = 0
    for x in range(0, 200):
        row = data.readline()
        row = row.split()
        row_reverse = row[::-1]
        for y in range(0, 320):
            if int(row[y]) != int(row_reverse[y]):
                # print(str(row[y])+" "+str(row_reverse[y]))
                result += 1
                break
    print("Ilość usuniętych wierszy: "+str(result))
    data.close()


def ex6_3():
    data = open("data/dane.txt", "r")
    condition = 128
    result = 0
    image = []
    for index in range(0, 200):
        row = data.readline()
        row = row.split()
        row = list(map(int, row))
        image.append(row)
    print("---------")
    for y in range(0, 200):
        for x in range(0, 320):
            if y == 0:
                if x == 0:
                    # left top corner
                    check1 = abs(image[y][x] - image[y][x+1])
                    check2 = abs(image[y][x] - image[y+1][x])
                    if check1 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                    if check2 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                elif x == 319:
                    # right top corner
                    check1 = abs(image[y][x] - image[y][x-1])
                    check2 = abs(image[y][x] - image[y+1][x])
                    if check2 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                    if check1 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                else:
                    # top edge
                    check1 = abs(image[y][x] - image[y][x+1])
                    check2 = abs(image[y][x] - image[y+1][x])
                    check3 = abs(image[y][x] - image[y][x-1])
                    if check1 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                    if check2 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                    if check3 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
            if y == 199:
                if x == 0:
                    # left bottom corner
                    check1 = abs(image[y][x] - image[y][x+1])
                    check2 = abs(image[y][x] - image[y-1][x])
                    if check1 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                    if check2 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                elif x == 319:
                    # right bottom corner
                    check1 = abs(image[y][x] - image[y][x-1])
                    check2 = abs(image[y][x] - image[y-1][x])
                    if check1 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                    if check2 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                else:
                    # bottom edge
                    check1 = abs(image[y][x] - image[y][x+1])
                    check2 = abs(image[y][x] - image[y][x-1])
                    check3 = abs(image[y][x] - image[y-1][x])
                    if check1 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                    if check2 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                    if check3 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
            if x == 0:
                if y != 0 and y != 199:
                    # left edge
                    check1 = abs(image[y][x] - image[y][x+1])
                    check2 = abs(image[y][x] - image[y+1][x])
                    check3 = abs(image[y][x] - image[y][x-1])
                    if check1 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                    if check2 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                    if check3 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
            if x == 319:
                if y != 0 and y != 199:
                    # right edge
                    check1 = abs(image[y][x] - image[y+1][x])
                    check2 = abs(image[y][x] - image[y][x-1])
                    check3 = abs(image[y][x] - image[y-1][x])
                    if check1 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                    if check2 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
                    if check3 > condition:
                        print("x="+str(x+1)+" y="+str(y+1))
                        print(image[y][x])
                        print("---------")
                        result += 1
            else:
                if y != 0 and y != 199:
                    if x != 0 and x != 319:
                        flag = False
                        check1 = abs(image[y][x] - image[y][x+1])
                        check2 = abs(image[y][x] - image[y+1][x])
                        check3 = abs(image[y][x] - image[y][x-1])
                        check4 = abs(image[y][x] - image[y-1][x])
                        if check1 > condition:
                            result += 1
                            if image[y][x] > image[y][x+1]:
                                flag = True
                        if check2 > condition:
                            result += 1
                            if image[y][x] > image[y+1][x]:
                                flag = True
                        if check3 > condition:
                            result += 1
                            if image[y][x] > image[y][x-1]:
                                flag = True
                        if check4 > condition:
                            result += 1
                            if image[y][x] > image[y-1][x]:
                                flag = True
                        if flag:
                            print("x=" + str(x + 1) + " y=" + str(y + 1))
                            print(image[y][x])
                            print("---------")
                            result -= 4
                            result += 1

    print(result)



# ex6_1()
# ex6_2()
ex6_3()
