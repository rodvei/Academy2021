# 1
ACCEPTED_OPERATORS = '+-*/'

print('EX4 Calculater!')
first_numb = input('Type the first number: ')
operator = input('Type an opteraotr (one of +, -, *, /): ')
second_numb = input('Type the second number: ')

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
print(result)

# 2
month_short = "Jan"

month_full = None
if month_short == "Jan":
    month_full = "January"
elif month_short == "Feb":
    month_full = "February"
elif month_short == "Dec":
    month_full = "December"
elif month_short == "Mar":
    month_full = "March"
elif month_short == "Apr":
    month_full = "April"
elif month_short == "May":
    month_full = "May"
elif month_short == "Jun":
    month_full = "June"
elif month_short == "Jul":
    month_full = "July"
elif month_short == "Aug":
    month_full = "August"
elif month_short == "September":
    month_full = "September"
elif month_short == "October":
    month_full = "October"
elif month_short == "Nov":
    month_full = "November"
else:
    month_full = "Unknow"

print(month_full)

# 4
import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)
dice4 = random.randint(1,6)
dice5 = random.randint(1,6)

print(f'dice values: {dice1}, {dice2}, {dice3}, {dice4} and {dice5}')
all_dice_equal = (dice1==dice2) and (dice1==dice3) and (dice1==dice4) and (dice1==dice5)
if all_dice_equal:
    print('Yahtzee')

# 5
bar_length = 10
current_number = 100
total_numb = 100

if (total_numb%10)==0:
    loaded_part = current_number/total_numb
    remaining_part = (total_numb-current_number)/total_numb
    loaded_length = loaded_part * bar_length
    remaining_length = remaining_part * bar_length

    loaded = '=' * (round(loaded_length)-1)
    remaining = ' ' * round(remaining_length)
    print(f'|{loaded}>{remaining}|')
else:
    print('Total_numb is not divisible by 10')
