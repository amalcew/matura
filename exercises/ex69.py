file = open("data/69/dane_geny.txt")
lines = file.readlines()
genotypes = []
genes = []
for line in lines:
    line = line.rstrip()
    genotypes.append(line)

# print(genotypes[0])


def extract(genotype):
    genotype = list(genotype)
    tmp = []
    a = 0
    b = 0
    flag = False
    already_true = False
    for x in range(len(genotype)):
        c = genotype[x]
        if c == "A":
            a += 1
        else:
            a = 0
        if c == "B":
            b += 1
        else:
            b = 0
        if a == 2:
            flag = True
            if not already_true:
                tmp.append("a")
            already_true = True
        if b == 2:
            flag = False
            already_true = False
            tmp.append("b")
            tmp.append(" ")

        if flag:
            tmp.append(c)

        # print(str(x)+". "+ genotype[x]+" - a:"+str(a)+" - b:"+str(b))
    tmp = ''.join(tmp)
    tmp = tmp.split()
    result = []
    for x in range(len(tmp)):
        codon = tmp[x].upper()
        end = codon[-2:]
        if end == "BB":
            result.append(codon)
            result.append(" ")
    if len(result) != 0:
        result.pop()
        return ''.join(result)


# print(extract("AACDBABBBCDAABCBBAAE"))
# print(extract("AADBAADDDDEEEBBEE"))
# print(extract("ABAEACBAADAACAABBABCDA"))
# print(extract("ABAEACBADEADACACABBABCDA"))


for x in range(len(genotypes)):
    g = extract(genotypes[x])
    genes.append(g)
    # print(str(x+1)+". "+g)


# 130 461
def ex69_1():
    print("zad1")
    genotypes_types = []
    quantity = []
    for x in range(len(genotypes)):
        type = "g"+str(len(genotypes[x]))
        genotypes_types.append(type)

    species = list(set(genotypes_types))
    for x in range(len(species)):
        type = species[x]
        quantity.append(genotypes_types.count(type))
    print("Number of species - "+str(len(species)))
    print("Max quantity of selected type - "+str(max(quantity))+"\n")


def ex69_2():
    print("zad2")
    mutation = "BCDDC"
    quantity = 0
    for x in range(len(genotypes)):
        genes = extract(genotypes[x])
        if mutation in genes:
            quantity += 1

    print("Specimens with mutation present - "+str(quantity)+"\n")


def ex69_3():
    print("zad3")
    quantity = []
    length = []
    for x in range(len(genotypes)):
        type_genes = genes[x].split()
        how_many_genes = len(type_genes)
        quantity.append(how_many_genes)
        for x in range(len(type_genes)):
            l = len(type_genes[x])
            length.append(l)
    print("Max number of genes - "+str(max(quantity)))
    print("Longest gene - "+str(max(length)))
    print()


def ex69_4():
    print("zad4")
    immune = 0
    strongly_immune = 0
    for x in range(len(genotypes)):
        genotype = genotypes[x]
        test1 = genotype[::-1]
        if genotype == test1:
            strongly_immune += 1
        else:
            gene = extract(genotype)
            gene = gene.replace(" ", "")
            test2 = extract(test1)
            if test2 is not None:
                test2 = test2.replace(" ", "")
            if test2 == gene:
                immune += 1

    print("Immune - "+str(immune))
    print("Strongly immune - "+str(strongly_immune))


ex69_1()
ex69_2()
ex69_3()
ex69_4()