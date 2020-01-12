from math import sqrt
# 120 453
file = open("data/63/ciagi.txt")
file = file.readlines()

lines = []

for line in file:
    lines.append(int(line))


def is_prime(number):
    num = number
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def zad1():
    print("zad 1:")
    for line in lines:
        if len(str(line)) % 2 == 0:
            w = str(line)
            l = len(w)/2
            w1 = w[0:int(l)]
            w2 = w[int(l)::]

            if w1 == w2:
                print(w1+" "+w2)
    print()


def zad2():
    k = 0
    for line in lines:
        flag = True
        w = str(line)
        for i in range(len(w)-1):
            a = w[i]
            b = w[i+1]
            if a == "1" and b == "1":
                flag = False
                break

        if flag:
            k +=1
    print("zad 2 - "+str(k)+"\n")


def zad3():
    k = []
    for line in lines:
        num = int(str(line), 2)
        if not is_prime(num):
            x = num - 1
            factors = []
            while True:
                if num % x == 0:
                    if is_prime(x):
                        factors.append(x)
                x -= 1
                if x == 1:
                    break
            if len(factors) == 2:
                if factors[0] * factors[1] == num:
                    k.append(num)
            elif len(factors) == 1:
                if factors[0]**2 == num:
                    k.append(num)
    print(len(k))
    print(max(k))
    print(min(k))

# zad1()
# zad2()
zad3()