# Задача 1
def number_max(*args):
    return max(args)


print(int(number_max(1, 5, 3)))


# Задача 2
def max_number2(a, b):
    return max(a, b)


def max_number3(a, b, c):
    two = max_number2(a, b)
    return max_number2(two, c)


print(max_number3(4, 9, 7))

# Задача 3
a = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
b = sorted(a, key=lambda x: x[1])
print(b)

# Задача 4
import datetime

now = datetime.datetime.now()
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
print(day(now))
print(month(now))
print(year(now))
