# Задача 2

def test_foo(a, b):
    return a ** b


try:
    test_foo(14, "2")
except Exception as e:
    print("Error", e)

try:
    test_foo(14, 5)
finally:
    print("The best result")

try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Error")


try:
    raise ZeroDivisionError
except ZeroDivisionError as y:
    print("Error")
finally:
    print("Reise, Reise, Seemann, reise! :D")


# Задача 3

def sum_num(a, b):
    return a / b


try:
    print(sum_num(6, "r"))
except ZeroDivisionError as e:
    print("ай яй яй делить на ноль можно не многим", e)
except Exception as e:
    print(e)
finally:
    print(" I 'am happy that you learn python")