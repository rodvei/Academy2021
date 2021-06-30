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