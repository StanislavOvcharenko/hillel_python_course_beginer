# Задача 1
def calculation(a):
    return((a + a + a + a), (a ** 2 + a ** 2) ** 0.5, (a * a))


print(calculation(8))


# Задача 2
def seasons(months):
    if months == 12 or months <= 2:
        print("Winter")
    elif months > 2 and months <= 5:
        print("Spring")
    elif months > 5 and months <= 8:
        print("Summer")
    elif months > 8 and months <= 11:
        print("Autumn")
    else:
        print("12 months in year :)")
    return


seasons(4)


# Задача 3
def list_concatenation(a=None, b=None):
    counter_a = 1
    counter_b = 0
    counter_i = len(a) + len(b)
    for c in a:
        if counter_a <= counter_i:
            a.insert(counter_a, b[counter_b])
            counter_a += 2
            counter_b += 1
    print(a)

list_concatenation(a=[1, 2, 3], b=[11, 22, 33])


# Задача 4
def polindrom(word):
    if word == word[::-1]:
        return True
    else:
        return False


print(polindrom("kkh"))
