data = open('dane/64/dane_obrazki.txt', 'r')

# Bit parzystości ciągu złożonego z zer i jedynek jest równy 0,
# gdy w ciągu tym występuje parzysta liczba jedynek, w przeciwnym
# razie bit parzystości jest równy 1


def ex64_1():
    """Konwersja obrazu i zapis do listy"""
    for x in range(0, 200):
        image = []
        for y in range(0, 22):
            line = data.readline()
            line = list(line)
            line.pop()
            if len(line) == 0:
                break
            line.pop()
            image.append(line)
        image.pop()

    """Odczyt obrazu z listy"""
    for y in range(0, 20):
        tmp_image = image[y]
        for xy in range(0, 222):
            print(tmp_image[xy])
ex64_1()
