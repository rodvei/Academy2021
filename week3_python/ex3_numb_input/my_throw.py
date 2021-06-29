import math

GRAVITY = 9.81

print('Calculate Throw length')

angle_degree = float(input('Type angle (in degrees): '))
velocity_kmh = float(input('Type velocity (in km/h): '))
throw_hight = float(input('Type throw height (in meter): '))

angle_radians = math.radians(angle_degree)
velocity_ms = velocity_kmh/3.6
velocity_ms_x = velocity_ms * math.cos(angle_radians)
velocity_ms_y = velocity_ms * math.sin(angle_radians)

sqrt_parth = math.sqrt(velocity_ms_y ** 2 + 2 * GRAVITY * throw_hight)
airtime = (velocity_ms_y + sqrt_parth)/GRAVITY

throw_length = velocity_ms_x * airtime
print(round(angle_radians, 2))
print(round(velocity_ms, 2))
print(round(velocity_ms_x, 2))
print(round(velocity_ms_y, 2))
print(round(airtime, 2))
print(round(throw_length, 2))
print(throw_length)

# less angles is optimal
# set velocity_kmh = 50 and throw_hight = 2
# then, throw_length is:
# angle_degree=44.9: 
#   throw_length -> 21.499248422912817
# angle_degree=45: 
#   throw_length -> 21.493474365706778
# angle_degree=45.1:
#   throw_length -> 21.4874765380616


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