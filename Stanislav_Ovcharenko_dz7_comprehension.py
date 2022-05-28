# list comprehension
a = [x * 5 for x in range(5)]
print(a)
b = [x / 2 * 3 for x in [8, 12, 14, 22, 51]]
print(b)
car = ["VW Golf", "MB C-class", "Audi a3"]
engine = ["1.6", "2.0", "2.2 Diesel"]
car_with_engine = [(z, x) for z in car for x in engine]
print(car_with_engine)
c = [x for x in range(5, 35, 5)]
print(c)
d = [x for x in range(-1, -11, -3)]
print(d)

# DICT comprehension
Car = {k: v for k, v in zip(car, engine)}
print(Car)
e = {k: k * 7 for k in range(5)}
print(e)
f = {k: v for k, v in zip(range(5), ["q", "w", "e", "r", "t"])}
print(f)
g = {k: len(k) for k in ["Python", "java", "C#"]}
print(g)
data_car = {"opel": "CADET", "skoda": "OCTAVIA", "lamborghini": "URUS"}
j = {k.upper(): v for k, v in data_car.items()}
print(j)

# set comprehensions
k = {x for x in range(10)}
print(k)
l = {x for x in [1, 1, 2, 5, 7, 7]}
print(l)
m = {len(x) for x in car}
print(m)
n = {x ** 3 for x in range(1,99,7)}
print(n)
o = {x * 3 / 9 for x in [1, 7, 9, 11]}
print(o)