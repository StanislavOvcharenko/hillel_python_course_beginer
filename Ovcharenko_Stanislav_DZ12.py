# # Задача 1
a = (x*2 for x in range(5))

def my_gen(n):
    while n <= 7:
        yield n + 1
        n += 1

def my_gen1(i):
    while len(i) < 15
        yield i + "a"
        i += "a"


# # Задача 2
 def my_reduce(function, ite, initializer=None):
     it_obj = iter(ite)                            # делаем из последовательности итератор
     if initializer == None:                       # если в initializer нет ничего берем следующее значение
         value = next(it_obj)
     else:
         value = initializer                       # придаем значение
     for i in it_obj:
         value = function(value, i)                # проходимся по последовательности и применяем функцию
     return value

# # Задача 3
def as_test(x):
    assert x <= 54
    return x

print(as_test((my_reduce(lambda x,y : x + y ,(1,2,3,4,5,6,7,8,9,10)))))

# Задача 4

class Car():
    def __init__(self, color, engine):
        self.color = color
        self.engine = engine

    def loc(self):
        return locals()

C1 = Car("red", "1.6")

print(C1.loc())