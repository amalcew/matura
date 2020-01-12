# 136 464
file = open("data/74/hasla.txt")
file = file.readlines()
passwords = []
for password in file:
    passwords.append(password[:-1])


def zad1():
    alphanumeric = []
    test = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for x in range(len(passwords)):
        password = str(passwords[x])
        flag = True
        for y in range(len(password)):
            letter = password[y]
            if letter not in test:
                flag = False
        if flag:
            alphanumeric.append(password)

    print("74.1 - "+str(len(alphanumeric)))
    print()


def zad2():
    print("74.2:")
    doubled = []
    for x in range(len(passwords)):
        password = passwords[x]
        k = passwords.count(password)
        if k >= 2:
            if password not in doubled:
                doubled.append(password)

    doubled = sorted(doubled)
    for x in range(len(doubled)):
        print(doubled[x])
    print()


def zad3():
    ascii = []
    for x in range(len(passwords)):
        password = passwords[x]
        flag = False
        for y in range(len(password)-3):
            s = [ord(password[y]), ord(password[y+1]), ord(password[y+2]), ord(password[y+3])]
            s = sorted(s)
            if s[3] - s[2] == 1 and s[2] - s[1] == 1 and s[1] - s[0] == 1:
                flag = True
        if flag:
            ascii.append(password)

    print("74.3 - "+str(len(ascii)))
    print()


def zad4():
    test = []
    for x in range(len(passwords)):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        password = list(passwords[x])
        flag1 = False
        flag2 = False
        flag3 = False
        for y in range(len(password)):
            letter = password[y]
            if letter in numbers:
                flag1 = True
            if letter.isupper():
                flag2 = True
            if letter.islower():
                flag3 = True
        if flag1 and flag2 and flag3:
            test.append(password)
    print("74.4 - "+str(len(test)))


zad1()
zad2()
zad3()
zad4()
