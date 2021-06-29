# 1.


my_name = r"""
    //   / /                      
   //__ / /    __     ( )  ___    
  //__  /    //  ) ) / / ((   ) ) 
 //   \ \   //      / /   \ \     
//     \ \ //      / / //   ) ) 
"""
print(my_name)


# 2.
my_name = 'Kristoffer'
last_name = 'Rodvei'
course = 'Academy data analytics'
numb_candidates = 100

text = f"""
My name is, {my_name}, with last name, {last_name}, 
I am participating in the course, {course}.There are, {numb_candidates} 
candidates taking the course."""
print(text)


# 3.
punishment_text = "Will not teach other to fly"
numb_of_repetition = 10

punishment_text = punishment_text.replace(' not ', ' ')
punishment_text = punishment_text.replace(' good ', ' bad ')

total_text = (punishment_text + '\n')*numb_of_repetition
print(total_text)

numb_of_that = punishment_text.upper().count('that')
print(f'The number of the word THAT in the original sentence is: {numb_of_that}')
