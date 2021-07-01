# 1.
months_converter = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}

month_short = "Jan"
full_month = months_converter.get(month_short, 'Unknown')
print(full_month)

# 2.
input_dict = {}
revert_dict = {}

is_running = True
while is_running:
    user_input = input('Seperated by ";" type a key; value pair:')
    if user_input.lower()=='revert':
        print(input_dict)
        for key, value in input_dict.items():
            revert_dict[value] = key
        print(revert_dict)
        is_running = False
    else:
        key, value = user_input.split(';')
        clean_key = key.strip()
        clean_value = value.strip()
        input_dict[clean_key] = clean_value

# 3.
# a)
dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}

concat_dict = {}
concat_dict.update(dict1)
concat_dict.update(dict2)
concat_dict.update(dict3)

# b)
input_dict = {
 'a':{'d':1, 'e':2},
 'b':{'f':3},
 'c':{'g':4, 'h':5}
}

unfolded_dict = {}
for key, value in input_dict.items():
    if isinstance(value, dict):
        for key_sub, value_sub in value.items():
            new_key = key + key_sub
            unfolded_dict[new_key] = value_sub
    else:
        unfolded_dict[key] = value

print(unfolded_dict)


# 4.

def set_by_path(input_dict, path, value):
    if len(path) == 1:
        current_value = value
    else:
        sub_dict = input_dict.get(path[0], {})
        current_value = set_by_path(sub_dict, path[1:], value)
    input_dict[path[0]] = current_value
    return(input_dict)

my_test = {'a':1}
my_test = set_by_path(my_test, ['b', 'c', 'd'], 2)
print(my_test)

# 5. self designed project based on API
