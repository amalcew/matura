system1hour = []
system1temperature = []
system2hour = []
system2temperature = []
system3hour = []
system3temperature = []

# binary system
system1 = open("dane/58/dane_systemy1.txt", "r")
for x in range(0, 1095):
    data = system1.readline()
    data = data[:-1]
    whitespace = data.find(" ")
    hour = data[0:whitespace]
    if hour != '':
        system1hour.append(int(hour, 2))
    temperature = data[whitespace+1:]
    if temperature != '':
        system1temperature.append(int(temperature, 2))

# quaternary system
system2 = open("dane/58/dane_systemy2.txt", "r")
for x in range(0, 1095):
    data = system2.readline()
    data = data[:-1]

    whitespace = data.find(" ")
    hour = data[0:whitespace]
    if hour != '':
        system2hour.append(int(hour, 4))
    temperature = data[whitespace+1:]
    if temperature != '':
        system2temperature.append(int(temperature, 4))

# octal system
system3 = open("dane/58/dane_systemy3.txt", "r")
for x in range(0, 1095):
    data = system3.readline()
    data = data[:-1]

    whitespace = data.find(" ")
    hour = data[0:whitespace]
    if hour != '':
        system3hour.append(int(hour, 8))
    temperature = data[whitespace+1:]
    if temperature != '':
        system3temperature.append(int(temperature, 8))


def ex58_1():
    print("Minimum recorded temperature from system 1 in decimal: "+str(min(system1temperature)))
    print("Minimum recorded temperature from system 2 in decimal: "+str(min(system2temperature)))
    print("Minimum recorded temperature from system 3 in decimal: "+str(min(system3temperature)))
    s1temp_bin = [bin(i) for i in system1temperature]
    # print("System 1 records in binary: "+str(s1temp_bin))
    s2temp_bin = [bin(i) for i in system2temperature]
    # print("System 2 records in binary: "+str(s2temp_bin))
    s3temp_bin = [bin(i) for i in system3temperature]
    # print("System 3 records in binary: "+str(s3temp_bin)+"\n")


def ex58_2():
    invalid_records = 0
    condition = 12
    for index in range(len(system1hour)):
        if system1hour[index] != condition and system2hour[index] != condition and system3hour[index] != condition:
            invalid_records += 1
            # print(str(system1hour[index])+" "+str(system2hour[index])+" "+str(system3hour[index]))
        condition += 24
    print("Invalid records quantity: "+str(invalid_records))


def ex58_3():
    record = False
    maxrecord1 = system1temperature[0]  # 0
    maxrecord2 = system2temperature[0]  # 5
    maxrecord3 = system3temperature[0]  # 5

    x = 1
    records = 1
    while x < 1094:
        if system1temperature[x] > maxrecord1:
            maxrecord1 = system1temperature[x]
            record = True
        if system2temperature[x] > maxrecord2:
            record = True
            maxrecord2 = system2temperature[x]
        if system3temperature[x] > maxrecord3:
            record = True
            maxrecord3 = system3temperature[x]
        if record == True:
            records += 1
        # print(str(maxrecord1)+" "+str(maxrecord2)+" "+str(maxrecord3))
        x += 1
        record = False
    print("Days including record temperature reading: "+str(records))


def ex58_4():
    t = []
    t.append("x")
    leaps = []
    for x in range(len(system1temperature)):
        t.append(system1temperature[x])
    for i in range(1,1095):
        for j in range(i+1, 1095):
            r = float(pow(t[i] - t[j], 2))
            difference = float(abs(i - j))
            leap = r//difference
            leap = round(leap)
            leaps.append(leap)
            # print("r = "+str(r)+", "+"diff = "+str(difference)+", "+"leap = "+str(leap))
    print("Maximal heat leap: "+str(max(leaps)))


ex58_1()
ex58_2()
ex58_3()
ex58_4()
