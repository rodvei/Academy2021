"""
2
Go to:
https://onlineasciitools.com/convert-text-to-ascii-art
and write your first name. Use font selection “Banner3” (you can select 
other, but the rest of the exercise becomes easier if none of the symbols /, 
\, ‘ or “ are used).
Make a python program that prints you name in this format.
"""
print('##    ## ########  ####  ######  ########  #######  ######## ######## ######## ########  ')
print('##   ##  ##     ##  ##  ##    ##    ##    ##     ## ##       ##       ##       ##     ## ')
print('##  ##   ##     ##  ##  ##          ##    ##     ## ##       ##       ##       ##     ## ')
print('#####    ########   ##   ######     ##    ##     ## ######   ######   ######   ########  ')
print('##  ##   ##   ##    ##        ##    ##    ##     ## ##       ##       ##       ##   ##   ')
print('##   ##  ##    ##   ##  ##    ##    ##    ##     ## ##       ##       ##       ##    ##  ')
print('##    ## ##     ## ####  ######     ##     #######  ##       ##       ######## ##     ## ')


"""
3.
a. Make a program that use appropriate variables for individual user 
information (at the placeholder X), and prints the following text
about the individual:
My name is
X
with last name
X. 
I am participating in the course
X
There are X
candidates taking the course.
b. Change some of the variables and re-run the code.
Imagine if this text was 200pages long, how many possible positions 
we must look through and change if we didn’t use variables!
Variables with descriptive names can be frustrating to make, but is 
very much worth it because of the redundancy and debuggability!
c. Change the print-function “end” parameter, such that the user 
variables are printed in text, and not on separate lines.

"""
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



"""
4.
At the top of your file write 
import time
and use “time.sleep(1)” between each print line (it makes python wait 1 
second between each print line). 
Make a load bar that start with the empty line
| |
for each second prints and extra load bar “=”, hence after 3second should 
look like this
|===> |
and ends with a full bar
|=========|
For all lines, use the print-function end-parameter
end = ”” (no new line)
and 
add “/r” in the beginning of each new print (revert the marker back to the 
beginning of the line).
This overwrite the text from the previous line (except the final line where 
you can use default end).
Finish by printing “Done!”
"""
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

"""
5.
Create a variable with the string:
my_string = ‘This iS a HEllO worLd test’
use “dir” to see what can be done with a string.
use “help” and learn how to use some of them.
particularly check out how to use “count” and “upper”/”lower” and count 
the number of L’s in the string (use the upper or lower such that you don’t 
have to search for both L’s and l’s)
"""
my_string = 'This iS a HEllO worLd test'
print(dir(my_string))
print(help(my_string.count))
print(help(my_string.upper))

numb_l = my_string.upper().count('L')
print(f'number of L\'s in the string is {numb_l}')