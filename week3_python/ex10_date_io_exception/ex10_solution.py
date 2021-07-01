# 1.
# a)
import os


def add_inputline(in_dict, line):
    key, value = line.split(';')
    clean_key = key.strip()
    clean_value = value.strip()
    in_dict[clean_key] = clean_value
    return(in_dict)

def revert_dict(in_dict):
    revert_dict = {}
    for key, value in in_dict.items():
        revert_dict[value] = key
    return(revert_dict)

def save_dict(in_dict, path):
    with open(path, mode='w') as file:
        for key, value in in_dict.items():
            file.write(f'{value};{key}\n')

def load_dict(path):
    out_dict = {}
    with open(path, mode='r') as file:
        for line in file:
            out_dict = add_inputline(out_dict, line)
    return(out_dict)

input_dict = {}
# Fancy way of getting script possition 
script_dir  = os.path.dirname(__file__)
save_path = os.path.join(script_dir, 'saved_dict.txt')
# hardcoding possition would also works like:
# save_path = r'C:\Users\krro\Academy2021\week3_python\ex10_date_io_exception\saved_dict.txt'
is_running = True
while is_running:
    user_input = input('Seperated by ";" type a key; value pair:')
    if user_input.lower()=='revert':
        print(input_dict)
        input_dict_revert = revert_dict(input_dict)
        print(input_dict_revert)
    elif user_input.lower()=='save':
        save_dict(input_dict, save_path)
    elif user_input.lower()=='load':
        input_dict = load_dict(save_path)
    elif user_input.lower()=='exit':
        is_running = False
    else:
        input_dict = add_inputline(input_dict, user_input)


# 2.
def my_calculator(first_numb, operator, second_numb)->float:
    result = None
    try:
        first_numb = float(first_numb)
        second_numb = float(second_numb)
        if operator == '+':
            result = first_numb + second_numb
        elif operator == '-':
            result = first_numb - second_numb
        elif operator == '*':
            result = first_numb * second_numb
        elif operator == '/':
            result = first_numb / second_numb
    except Exception as e:
        print(f'Error, something went wrong {e}')
    return(result)

first_numb = input('Type the first number: ')
operator = input('Type an opteraotr (one of +, -, *, /): ')
second_numb = input('Type the second number: ')

output = my_calculator(first_numb, operator, second_numb)
print(output)
