# 137
# 465
text = open("data/75/tekst.txt")
text = text.readline()
text = text.split()

table = {}
k = 0
for x in range(97, 123):
    table[chr(x)] = k
    k += 1

print(table)

def ex75_1():
    for x in range(len(text)):
        word = text[x]
        if word[0] == "d" and word[-1] == "d":
            print(word)

