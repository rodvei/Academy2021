# 1.
# a)
var_1, var_2, var_3 = 1, 2, 3
# b)
temp = var_2
var_2 = var_1
var_1 = var_2
# c)
var_1, var_2 = var_2, var_1


# 2.
# a)
captured = ('Pikachu', 'Pidgey', 'Abra', 'Pidgey', 'Eevee', 'Pidgey')
# b)
# If we want to add pokemons to our captured varaible, than list would
# be benificial

# c)
captured.count('Pidgey')

# d)
unique_capture = set(captured)
new_pokemon = input('Type the name of the pokemon: ')

if new_pokemon in unique_capture:
    print('Already got it')
else:
    print('This is a new pokemon!')

# 3.
import numpy as np
import scipy.stats as stats

GRAVITY = 9.81

n=100
throw_hight = 1.88
velocity_kmh = stats.weibull_max.rvs(2,loc=107, scale=4, size=n)
angle_degree = stats.norm.rvs(loc=48, scale=7, size=n)

angle_radians = np.radians(angle_degree)
velocity_ms = velocity_kmh/3.6
velocity_ms_x = velocity_ms * np.cos(angle_radians)
velocity_ms_y = velocity_ms * np.sin(angle_radians)

sqrt_parth = np.sqrt(velocity_ms_y ** 2 + 2 * GRAVITY * throw_hight)
airtime = (velocity_ms_y + sqrt_parth)/GRAVITY

throw_length = velocity_ms_x * airtime

# c
alpha = 0.05
my_sorted_list = sorted(throw_length)

n = len(throw_length)
lower_idx = round(n*alpha/2)
upper_idx = round(n*(1-alpha/2)-1)

print(f'lower limit = {my_sorted_list[lower_idx]}')
print(f'uppper limti = {my_sorted_list[upper_idx]}')

# d EXTRA HARD:
n=6000
velocity_kmh = stats.weibull_max.rvs(2,loc=107, scale=4, size=n)
angle_degree = stats.norm.rvs(loc=48, scale=7, size=n)
velocity_kmh = velocity_kmh.reshape(1000,6)
angle_degree = angle_degree.reshape(1000,6)

angle_radians = np.radians(angle_degree)
velocity_ms = velocity_kmh/3.6
velocity_ms_x = velocity_ms * np.cos(angle_radians)
velocity_ms_y = velocity_ms * np.sin(angle_radians)

sqrt_parth = np.sqrt(velocity_ms_y ** 2 + 2 * GRAVITY * throw_hight)
airtime = (velocity_ms_y + sqrt_parth)/GRAVITY

throw_length = velocity_ms_x * airtime

# we now have 1000 games with 6 throw in each
print(throw_length.shape)
# max of each game (row wise, if axis=0 would give colum wise)
max_throw_length = np.max(throw_length, axis = 1)
print(max_throw_length.shape)

# calculate numerical confidence interval
alpha = 0.05
my_sorted_list = sorted(max_throw_length)

n = len(max_throw_length)
lower_idx = round(n*alpha/2)
upper_idx = round(n*(1-alpha/2)-1)

print(f'lower limit = {my_sorted_list[lower_idx]}')
print(f'uppper limti = {my_sorted_list[upper_idx]}')
