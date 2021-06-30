# 1.
# a
students = ['Kristoffer Rodvei', 'Snorre husby', 'Jan Johansen', 'Ola Nordmann', 'Kari Hansen']

third_person_origin = students[2]
# b
print(students[2])
# c
print(students[2][0])
# d
students[2] = 'Ole'
# e
students[2] = students[2] + ' Nordmann'
# f
students.append(third_person_origin)
# g
students.insert(4, 'Monty Python')
# h
print(len(students))
students.remove('Ole Nordmann')
print(len(students))
# i
monty_python_idx = students.index('Monty Python')
print(monty_python_idx)
# j
print(students[0:3])
# k
students_reverse = students[::-1]
# l
students_even = students[::2]
# m
students_odd = students[1::2]


# 2.
import random
dice = [1,2,3,4,5,6]
n_dices = 5
rand_dices = random.choices(dice, k=5)

all_equal = (rand_dices[0]==rand_dices[1]) and ((rand_dices[0]==rand_dices[2])) and (rand_dices[0]==rand_dices[3]) and (rand_dices[0]==rand_dices[4]) and (rand_dices[0]==rand_dices[5])

if all_equal:
    print('Yahtzee!')

print(f'The lowest value is {min(all_equal)}')
print(f'The biggest value is {max(all_equal)}')
print(f'Dices, sorted: {sorted(all_equal)}')


# 3.
my_list = [1,5,2,6,8,4,6,3,6,8,55,2,5,7,8,9,3,1,32,89,3,2,5,8,4,2,6,8,5,2,5,8]
alpha = 0.05

my_sorted_list = sorted(my_list)

n = len(my_list)
lower_idx = round(n*alpha/2)
upper_idx = round(n*(1-alpha/2)-1)

print(f'lower limit = {my_sorted_list[lower_idx]}')
print(f'uppper limti = {my_sorted_list[upper_idx]}')

# 4.
list_of_lists = [1, [2, 3,'4'], [5, [6, '7', 8], 9, 10]]
list_of_lists[1][2]=4
list_of_lists[2][1][1]=7

