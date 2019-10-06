
data = open('dane/61/ciagi.txt', 'r')


def ex61_1():
    differences = []
    arithmetic_sequences = []
    for x in range(1,101):
        elements_amount = data.readline()
        elements_amount = int(elements_amount)

        sequence_raw = data.readline()
        sequence_raw = sequence_raw[:-1]
        sequence = sequence_raw.split(' ')

        different = int(sequence[1]) - int(sequence[0])
        x = 1
        condition = True
        while x < elements_amount:
            if int(sequence[x]) - int(sequence[x-1]) != different:
                condition = False
                break
            x += 1
        if condition:
            differences.append(different)
            arithmetic_sequences.append(sequence)

    print("Number of arithmetic sequences: "+str(len(arithmetic_sequences)))
    print("Max difference: "+str(max(differences)))


def ex61_2():
    max_root = []
    for x in range(1, 101):
        max_root_temp = []
        elements_amount = data.readline()
        elements_amount = int(elements_amount)

        sequence_raw = data.readline()
        sequence_raw = sequence_raw[:-1]
        sequence = sequence_raw.split(' ')

        for y in range(0, elements_amount):
            root = pow(int(sequence[y]), 1/3)
            pz = int(round(root))
            if pz**3 == int(sequence[y]):
                max_root_temp.append(int(sequence[y]))

        if len(max_root_temp) != 0:
            max_root.append(max(max_root_temp))

    print(max_root)


# ex61_1()
ex61_2()
