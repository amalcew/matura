file = open("dane/dane4.txt")
file = file.readlines()
numbers = []
for line in file:
    numbers.append(int(line))


def zad4_1():
    print("4.1")
    gaps = []
    for x in range(len(numbers)-1):
        a = numbers[x]
        b = numbers[x+1]
        gaps.append(abs(a-b))
    print("Min - "+str(min(gaps)))
    print("Max - " + str(max(gaps)))
    print()


def zad4_2():
    print("4.2")
    # numbers = [4, 11, 4, 1, 4, 7, 10, 11, 12, 13, 14, 7, 0, 3]
    gaps = []
    length = 1
    max_length = 1
    sequence = []
    max_sequence = []

    for x in range(0, len(numbers) - 1):
        gap = abs(numbers[x] - numbers[x + 1])
        gaps.append(gap)
        sequence.append(numbers[x])
        if len(gaps) != 0:
            if gaps[x - 1] == gaps[x]:
                length += 1
            else:
                sequence.insert(0, numbers[x-length])
                if max_length < length:
                    max_length = length
                    max_sequence = sequence

                length = 1
                sequence = []

    print("Max length: " + str(max_length + 1))
    # print(max_sequence)
    print("Start: "+str(max_sequence[0]))
    print("End: "+str(max_sequence[-1]))
    print()


def zad4_3():
    gaps = []
    # numbers = [4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3]
    for x in range(len(numbers)-1):
        a = numbers[x]
        b = numbers[x+1]
        gaps.append(abs(a-b))
    gaps = sorted(gaps)
    unique_gaps = list(set(gaps))
    most_common = 0
    lst_of_most_common = []
    for x in range(len(unique_gaps)):
        tmp = gaps.count(unique_gaps[x])
        if tmp > most_common:
            most_common = tmp
    for x in range(len(unique_gaps)):
        tmp = gaps.count(unique_gaps[x])
        if tmp == most_common:
            lst_of_most_common.append(unique_gaps[x])

    print("Most common: "+str(most_common))
    print("List of most common: "+str(lst_of_most_common))


zad4_1()
zad4_2()
zad4_3()
