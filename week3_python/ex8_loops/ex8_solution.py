# 1.
# a)
def bart_cheat_code_while(punishment_text, numb_of_repetition=10):
    total_text = ''
    counter = 0
    while numb_of_repetition>counter:
        total_text = total_text + f'{punishment_text}\n'
        counter = counter + 1
    return(total_text)

# b)
def bart_cheat_code_for(punishment_text, numb_of_repetition=10):
    total_text = ''
    counter = 0
    for _ in range(0, numb_of_repetition):
        total_text = total_text + f'{punishment_text}\n'
    return(total_text)

punishment_text = "Will not teach other to fly"
numb_of_repetition = 17

while_text = bart_cheat_code_while(punishment_text, numb_of_repetition)
print(while_text)

for_text = bart_cheat_code_for(punishment_text, numb_of_repetition)
print(for_text)

# 2.
target_number = 15
guesses_allowed = 10

is_running = True
count = 0
while is_running:
    guess = int(input('Guess my number :'))
    count = count + 1
    if guess==target_number:
        print('hey!, you found it!')
        is_running = False
    elif count>=guesses_allowed:
        print('Sorry, you\'re out of tries')
        is_running = False
    elif guess>target_number:
        print(f'Smaller and you have used {count}/{guesses_allowed} guesses')
    elif guess<target_number:
        print(f'Larger and you have used {count}/{guesses_allowed} guesses')
    else:
        print('error')

# 3.
for i in range(0,101,1):
    if i%15==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

# Alternativly a one-liner, if you're into that: 
print(['Fizz'*(i%3==0)+'Buzz'*(i%5==0) or i for i in range(1,101)])


# 4.
# Some functions from last ex7:
import math


def kmh_to_ms(kmh):
    return(kmh/3.6)

def velocity_decomposition(velocity, angle)->tuple:
    velocity_horizontal = velocity * math.cos(angle)
    velocity_vertical = velocity * math.sin(angle)
    return(velocity_horizontal, velocity_vertical)

def airtime(velocity_y, init_height, g=9.81):
    sqrt_parth = math.sqrt(velocity_y**2 + 2*g*init_height)
    airtime = (velocity_y + sqrt_parth)/g
    return(airtime)

def throw_distance(velocity, angle, init_height=1.8)->float:
    """Calculates throw distance

    Args:
        velocity (float): Velocity in km/h.
        angle (flaot): Angle in degrees.
        init_height (float, optional): Initial throw hight (compared to landing
            hight) in meters. Defaults to 1.8.

    Returns:
        float: Throw distance
    """
    angle_radians = math.radians(angle)
    velocity_ms = kmh_to_ms(velocity)
    velocity_ms_x, velocity_ms_y = velocity_decomposition(velocity_ms, angle_radians)
    throw_airtime = airtime(velocity_ms_y, init_height)
    throw_length = velocity_ms_x * throw_airtime
    return(throw_length)

def quantile(series, alpha=0.05)->tuple:
    """Calculate the upper and lower alpha quantile of the series.

    Args:
        series (list): List of values.
        alpha (float, optional): Alpha, defined as the part of the data 
            outside the intervall. Defaults to 0.05 => 95% numerial 
            confidence interval

    Returns:
        tuple: Two number in a tuple, (lower_limit, upper_limit).
    """
    sorted_series = sorted(series)
    n = len(sorted_series)
    lower_idx = round(n*alpha/2)
    upper_idx = round(n*(1-alpha/2)-1)
    lower_lim = sorted_series[lower_idx]
    upper_lim = sorted_series[upper_idx]
    return(lower_lim, upper_lim)


# solution for ex 8:
# a)
import scipy.stats as stats
import matplotlib.pyplot as plt

def thorkildsen_throw():
    velocity = stats.weibull_max.rvs(2, loc=107, scale=4, size=1)[0]
    angle = stats.norm.rvs(48, 7, 1)[0]
    throw_len = throw_distance(velocity, angle, 1.88)
    return(throw_len)

def pitkamaki_throw():
    velocity = stats.weibull_max.rvs(2, loc=106.5, scale=3, size=1)[0]
    angle = stats.norm.rvs(45.5, 4, 1)[0]
    throw_len = throw_distance(velocity, angle, 1.88)
    return(throw_len)

# b)
def thorkildsen_competion_best(numb_throw=6):
    throw_lens = []
    for i in range(numb_throw):
        throw_lens.append(thorkildsen_throw())
    best_throw = max(throw_lens)
    return(best_throw)

def pitkamaki_competion_best(numb_throw=6):
    throw_lens = []
    for i in range(numb_throw):
        throw_lens.append(pitkamaki_throw())
    best_throw = max(throw_lens)
    return(best_throw)

# c)
numb_sim = 1000
thorkildsen_results = []
pitkamaki_results = []
for i in range(numb_sim):
    thorkilsen_best = thorkildsen_competion_best()
    thorkildsen_results.append(thorkilsen_best)
    pitkamaki_best = pitkamaki_competion_best()
    pitkamaki_results.append(pitkamaki_best)

plt.hist(thorkildsen_results, bins=50, alpha=0.5, label="Thorkilsen")
plt.hist(pitkamaki_results, bins=50, alpha=0.5, label="Pitkamaki")
plt.legend(loc='upper right')
plt.show()

# d)
thorkildsen_limit = quantile(thorkildsen_results, alpha=0.05)
pitkamaki_limit = quantile(pitkamaki_results, alpha=0.05)
print(f'Thorkildsens 95p interval is {thorkildsen_limit}')
print(f'Pitkamaki 95p interval is {pitkamaki_limit}')

# e)
numb_sim = 1000
thorkildsen_results = []
pitkamaki_results = []
for i in range(numb_sim):
    thorkilsen_best = thorkildsen_competion_best(18)
    thorkildsen_results.append(thorkilsen_best)
    pitkamaki_best = pitkamaki_competion_best(18)
    pitkamaki_results.append(pitkamaki_best)

plt.hist(thorkildsen_results, bins=50, alpha=0.5, label="Thorkilsen")
plt.hist(pitkamaki_results, bins=50, alpha=0.5, label="Pitkamaki")
plt.legend(loc='upper right')
plt.show()

thorkildsen_limit = quantile(thorkildsen_results, alpha=0.05)
pitkamaki_limit = quantile(pitkamaki_results, alpha=0.05)
print(f'Thorkildsens 95p interval is {thorkildsen_limit}')
print(f'Pitkamaki 95p interval is {pitkamaki_limit}')

