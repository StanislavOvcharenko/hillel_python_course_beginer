# Задача 1

# Способ 1
password = input("Fill up your password")
password1 = input("Confirm your password")
if password == password1:
    print("welcome")
else:
    print("Please try again")

# Способ 2
password = input("Fill up your password")
password1 = input("Confirm your password")

for numbers in password:
    if password1 == password:
        print("Welcome")
        break
    else:
        print("please try again")
    break

# Задача 2

Products = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
i = "eg"
while i in Products:
    Products.remove("eg")
print(Products)

# Задача 3

numbers = [11, 23, 65, 44, 76, 533]

for key in numbers:
    key == int(key)

while key in numbers:
    if key % 2 == 0:
        print("all numbers are even")
        break
    else:
        print("NO")
        break

# Задача 4

new_object = dir(set)
methods = list(new_object)
clear_methods = [q for q in methods if not q.startswith('__')]
print(clear_methods)

# Задача 6
my_set3 = set("python")
my_set2 = set("hello")
my_set = set("1,2,3,4,5,6,7")
# add
my_set.add(8)
# copy
my_set1 = my_set.copy()
# clear
my_set1.clear()
# difference
my_set3.difference(my_set, my_set2)
# difference_update
my_set3.difference_update(my_set)
# discard
my_set.discard("1")
# intersection
a = my_set.intersection(my_set1)
# intersection_update
m = set("hello")
n = set("hello world")
n.intersection_update(m)
# isdisjoint
l = set("ljop")
k = set("ktur")
print(l.isdisjoint(k))
# issubset
print(l.issubset(k))
# issuperset
print(k.issuperset(l))
# pop
g = my_set.pop()
print(g)
# remowe
k.remove("k")
print(k)
# symmetric_difference
b = my_set.symmetric_difference(my_set3)
print(b)
# symmetric_difference_update
nm = set("12345")
mn = set("56789")
nm.symmetric_difference_update(mn)
print(nm)
# union
oo = set("123")
pp = set("456")
vv = oo.union(pp)
print(vv)
# update
o1 = set("123")
o2 = set("456")
o3 = set()
o3.update(o1, o2)
print(o3)
