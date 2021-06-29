# 2.
print('##    ## ########  ####  ######  ########  #######  ######## ######## ######## ########  ')
print('##   ##  ##     ##  ##  ##    ##    ##    ##     ## ##       ##       ##       ##     ## ')
print('##  ##   ##     ##  ##  ##          ##    ##     ## ##       ##       ##       ##     ## ')
print('#####    ########   ##   ######     ##    ##     ## ######   ######   ######   ########  ')
print('##  ##   ##   ##    ##        ##    ##    ##     ## ##       ##       ##       ##   ##   ')
print('##   ##  ##    ##   ##  ##    ##    ##    ##     ## ##       ##       ##       ##    ##  ')
print('##    ## ##     ## ####  ######     ##     #######  ##       ##       ######## ##     ## ')


# 3.
my_name = 'Kristoffer'
last_name = 'Rodvei'
course = 'Academy data analytics'
numb_candidates = 100

print('My name is,', end=' ')
print(my_name, end=', ')
print('with last name,', end=' ')
print(last_name, end=', ') 
print('I am participating in the course,', end=' ')
print(course, end=', ')
print('There are,', end=' ')
print(numb_candidates, end=', ')
print('candidates taking the course.')



# 4.
import time

print('\r|          |', end='')
time.sleep(1)
print('\r|>         |', end='')
time.sleep(1)
print('\r|=>        |', end='')
time.sleep(1)
print('\r|==>       |', end='')
time.sleep(1)
print('\r|===>      |', end='')
time.sleep(1)
print('\r|====>     |', end='')
time.sleep(1)
print('\r|=====>    |', end='')
time.sleep(1)
print('\r|======>   |', end='')
time.sleep(1)
print('\r|=======>  |', end='')
time.sleep(1)
print('\r|========> |', end='')
time.sleep(1)
print('\r|=========>|', end='')
time.sleep(1)
print('\r|==========|')
print('Done!')

# 5.
my_string = 'This iS a HEllO worLd test'
print(dir(my_string))
print(help(my_string.count))
print(help(my_string.upper))

numb_l = my_string.upper().count('L')
print(f'number of L\'s in the string is {numb_l}')