"""
Na początku chciałem rozwiązać to zadanie przy pomocy funkcji rekurencyjnej fibonacciego, ale co ciekawe, generowanie
kolejnych wyrazów ciągu poprzez rekurencję trwało niewiarygodnie długo. Użycie prostej pętli 'while' z listą zawierającą
dwa pierwsze wyrazy ciągu rozwiązuje ten problem
"""
fibonacci = [0, 1]
while True:
    a = fibonacci[-2]
    b = fibonacci[-1]
    c = a + b
    if c > 10**9:
        break
    # print(c)
    fibonacci.append(c)

file = open("data/dane.txt")
file = file.readlines()
answer = open("zadanie5.txt", "w")
answer.close()
numbers = []
for line in file:
    numbers.append(int(line))

# task 1
answer = open("zadanie5.txt", "a")
answer.write("a\n")
answer.close()
correct = []
for x in range(len(numbers)):
    number = numbers[x]
    if number in fibonacci:
        # print(number)
        correct.append(number)
        answer = open("zadanie5.txt", "a")
        answer.write(str(number)+"\n")
        answer.close()

# task 2
answer = open("zadanie5.txt", "a")
answer.write("\nb\n")
answer.write(str(min(correct))+"\n")
answer.write(str(max(correct))+"\n")
answer.close()

# task 3
answer = open("zadanie5.txt", "a")
answer.write("\nc\n")
answer.close()
sequence = []
for x in range(len(correct)):
    a = correct[x]
    tmp = [a]
    # print(str(x)+" s "+str(a))
    for y in range(len(correct)):
        if y > x:
            b = correct[y]
            if b > a:
                tmp.append(b)
                # print(str(y)+" + "+str(b))
                a = b
            # else:
                # print(str(y)+" - "+str(b))
    # print("end")
    if len(tmp) > len(sequence):
        sequence = tmp

for x in range(len(sequence)):
    answer = open("zadanie5.txt", "a")
    answer.write(str(sequence[x])+"\n")
    answer.close()

print("done")
