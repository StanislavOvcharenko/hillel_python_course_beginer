# Задача 1
#first = {1: 10, 2: 20}
#second = {3: 30, 4: 40}
#third = {5: 50, 6: 60}
#fourth = {7: 70, 8: 80}
#fifth = {9: 90, 10: 100}

#a = (first, second, third, fourth, fifth)

#numbers = {}
#for i in a:
#    numbers.update(i)
#
#print(numbers)

# Задача 2
#dict_a = {k:k**2 for k in range(11, 21)}
#print(dict_a)
#sum_dict_a = sum(list(dict_a.values()))
#print(sum_dict_a)

# Задача 3
#any_dict = {6:"subaru",
#            5:"BMW",
#            4:"Mercedes",
#            3:"VW",
#            2:"Audi",
#            1:"SKoda"
#}

#sort_any_dict = sorted(any_dict)
#print(sort_any_dict)


# Задача 4
#id ={'id1':
#{
#'name': 'Ruslan',
#'class': 1,
#'subjects' : {'Math', 'Algorithms', 'English'}
#},
#'id2':
#{
#'name': 'Mark',
#'class': 2,
#'subjects' : {'Geometry', 'Java', 'Cooking'}
#},
#'id3':
#{
#'name': 'Ruslan',
#'class': 1,
#'subjects' : {'Math', 'Algorithms', 'English'}
#}}
#print(id.items())
#unique_id = {}
#for k, v in id.items():
#    if v not in unique_id.values():
#        unique_id[k] = v
#print(unique_id)

#Задача 5
#list_5 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"},
#              {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#
#value_list = list()
#for v in list_5:
#    value_list += list(v.values())
#print(set(value_list))

#Задача 6
shedule = {'monday': ['clean house', 'drive car', 'meet with freands'],
           'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}

count = (sum([len(shedule[c]) for c in shedule if isinstance(shedule[c], list)]))
print(count)