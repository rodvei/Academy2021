# 1.
def say_my_name()->None:
    """Prints Kris in cool text format
    """
    my_name = r"""
        //   / /                      
       //__ / /    __     ( )  ___    
      //__  /    //  ) ) / / ((   ) ) 
     //   \ \   //      / /   \ \     
    //     \ \ //      / / //   ) ) 
    """
    print(my_name)

say_my_name()


# 2.
def bart_cheat_code(punishment_text, numb_of_repetition=10)->str:
    total_text = (punishment_text + '\n')*numb_of_repetition
    return(total_text)

punishment_text = "Will not teach other to fly"
numb_of_repetition = 17

bart_full_text = bart_cheat_code(punishment_text, numb_of_repetition)
print(bart_full_text)

test_defuatl = bart_cheat_code(punishment_text)
print(test_defuatl)


# 3.
def my_calculator(first_numb, operator, second_numb)->float:
    ACCEPTED_OPERATORS = '+-*/'
    result = None
    # should be a single operator and one of +,-,*,/
    operator_length_valid = len(operator)==1
    operator_value_valid = operator in ACCEPTED_OPERATORS
    operator_valid = operator_length_valid and operator_value_valid
    numb_valid = first_numb.isnumeric() and second_numb.isnumeric()
    if not operator_valid:
        print(f'Error, operator {operator} is not valid')
    elif not numb_valid:
        print(f'Error, number {first_numb} or {second_numb} not valid')
    else:
        first_numb = int(first_numb)
        second_numb = int(second_numb)
        if operator == '+':
            result = first_numb + second_numb
        elif operator == '-':
            result = first_numb - second_numb
        elif operator == '*':
            result = first_numb * second_numb
        elif operator == '/':
            if second_numb==0:
                print('Error, cannot devide with zero')
            else:
                result = first_numb / second_numb        
    return(result)


first_numb = input('Type the first number: ')
operator = input('Type an opteraotr (one of +, -, *, /): ')
second_numb = input('Type the second number: ')

output = my_calculator(first_numb, operator, second_numb)
print(output)


# 4. 
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

def throw_possition(velocity, angle, time, init_height=1.8)->float:
    """Calculates throw possition

    Args:
        velocity (float): Velocity in km/h.
        angle (flaot): Angle in degrees.
        time (float): The time for calculating throw possition.
        init_height (float, optional): Initial throw hight (compared to landing
            hight) in meters. Defaults to 1.8.

    Returns:
        float: Throw possition
    """
    angle_radians = math.radians(angle)
    velocity_ms = kmh_to_ms(velocity)
    velocity_ms_x, velocity_ms_y = velocity_decomposition(velocity_ms, angle_radians)
    throw_airtime = airtime(velocity_ms_y, init_height)
    if throw_airtime>=time:
        throw_length = velocity_ms_x * time
    else:
        throw_length = throw_distance(velocity, angle, init_height)
    return(throw_length)

throw_example = throw_distance(50, 30, 2)
print(throw_example)

throw_example_pos = throw_possition(50, 30, 1, 2)
print(throw_example_pos)

# 5.
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

my_list = [1,5,2,6,8,4,6,3,6,8,55,2,5,7,8,9,3,1,32,89,3,2,5,8,4,2,6,8,5,2,5,8]
print(quantile(my_list))