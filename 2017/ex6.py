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
            pixel = image[y][x]
            # top edge
            if y == 0:
                # left top corner
                if x == 0:
                else:
            # left edge
            if x == 0:
                # left bottom corner
                if y == 319:
                else:
            # bottom edge
            if y == 319:
                # right bottom corner
                if x == 199:
                else:
            # right edge
            if x == 199:
                # right top corner
                if y == 0:
                else:
            # inner pixel
            else:



# ex6_1()
# ex6_2()
ex6_3()
