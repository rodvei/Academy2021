"""
1.
Go back to ex_print_and_var.docx exercise 2, and redo the task using 
multiline R-string and pick any another layout where “/” symbol is also used"""

my_name = r"""
    //   / /                      
   //__ / /    __     ( )  ___    
  //__  /    //  ) ) / / ((   ) ) 
 //   \ \   //      / /   \ \     
//     \ \ //      / / //   ) ) 
"""
print(my_name)

"""
2.
a) Go back to ex_print_and_var.docx exercise 3, and redo the task using 
a multi-line F-string (making the solution code simpler and easier to 
understand)
b) Even if the variables for the first and last name is written with the 
wrong format (upper and lower cases), make sure they are printed 
with the first letter being upper case and the rest as lower case.
c) Make sure the course name is printed using all lower cases.
"""
my_name = 'Kristoffer'
last_name = 'Rodvei'
course = 'Academy data analytics'
numb_candidates = 100

text = f"""
My name is, {my_name}, with last name, {last_name}, 
I am participating in the course, {course}.There are, {numb_candidates} 
candidates taking the course."""
print(text)

"""
3.
Write a program that helps Bart Simpson. 
a. By specifying the variables 
“punishment_text”
and
“numb_of_repetition”
the program should print the same “punishment_text” the 
“numb_of_repetition” just like you see in the picture.
Use anything learned until now (while/for loops and lists are prohibited in this exercise). Remember to add a line shift (“/n”) for 
each time punishment line is written.
b. Mess with Bart, by writing code that removing the word “not” in 
“punishment_text”, and changing the word “good” with “bad” 
before its printed out.
c. Bart has a bad habit of using the word “that” to often. Add logic to 
the code such that the number of the word “that” is counted in 
“punishment_text”. Then after the multiple lines of 
“punishment_text” is printed, a single line with the information is 
printed with the following format
“The number of the word THAT in the original sentence is: X”, 
with X replaced by the number
"""
punishment_text = "Will not teach other to fly"
numb_of_repetition = 10

punishment_text = punishment_text.replace(' not ', ' ')
punishment_text = punishment_text.replace(' good ', ' bad ')

total_text = (punishment_text + '\n')*numb_of_repetition
print(total_text)

numb_of_that = punishment_text.upper().count('that')
print(f'The number of the word THAT in the original sentence is: {numb_of_that}')
