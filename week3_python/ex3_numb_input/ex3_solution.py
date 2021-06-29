# 1.
my_name = input('Write first name: ')
last_name = input('Write last name: ')
course = input('Write your course: ')
numb_candidates = int(input('Write the number of candidates'))

text = f"""
My name is, {my_name}, with last name, {last_name}, 
I am participating in the course, {course}.There are, {numb_candidates} 
candidates taking the course."""
print(text)


# 3.
bar_length = 10
current_number = 100
total_numb = 100

loaded_part = current_number/total_numb
remaining_part = (total_numb-current_number)/total_numb
loaded_length = loaded_part * bar_length
remaining_length = remaining_part * bar_length

loaded = '=' * (round(loaded_length)-1)
remaining = ' ' * round(remaining_length)
print(f'|{loaded}>{remaining}|')