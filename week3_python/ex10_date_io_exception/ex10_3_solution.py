# 3.
# a)
import os
import datetime

# Fancy way of getting script possition 
script_dir  = os.path.dirname(__file__)
goog_path = os.path.join(script_dir, 'GOOG.csv')
# hardcoding possition would also works, like:
# save_path = r'C:\Users\krro\Academy2021\week3_python\ex10_date_io_exception\GOOG.csv'
with open(goog_path, mode='r') as google_file:
    for i in range(15):
        print(google_file.readline())
# prints:
# Date,Open,High,Low,Close,Adj Close,Volume
# 2020-07-01,1411.099976,1443.000000,1409.819946,1438.040039,1438.040039,1775200
# 2020-07-02,1446.939941,1482.949951,1446.420044,1464.699951,1464.699951,1859100
# .
# .
# .


# b)
def get_line_info(line):
    data = {}
    date = None
    try:
        line_list = line.split(',')
        date = datetime.datetime.strptime(line_list[0], '%Y-%m-%d').date()
        data['Open'] = float(line_list[1])
        data['High'] = float(line_list[2])
        data['Low'] = float(line_list[3])
        data['Close'] = float(line_list[4])
        data['Adj Close'] = float(line_list[5])
        data['Volume'] = int(line_list[6])
    except Exception as e:
        print(f'Failed, bad line: {line}')
    return(date, data)

# c)
data = {}
with open(goog_path, mode='r') as google_file:
    # first line is header
    header = google_file.readline()
    # after header is taken out, loop through rest
    for line in google_file: 
        date, date_data = get_line_info(line)
        if date is not None:
            data[date] = date_data

# e)
max_diff = -1
date_of_max_diff = None
for date, date_data in data.items():
    diff = date_data['High']-date_data['Low']
    if diff>max_diff:
        max_diff = diff
        date_of_max_diff = date
print(f'On {date_of_max_diff} we had a max high/low diff of {max_diff}')

# f)
max_value = -1
date_of_max_val = None
for date, date_data in data.items():
    if date_data['High']>max_value:
        max_value = date_data['High']
        date_of_max_val = date
print(f'On {date_of_max_val} we had the largest stock prie of {max_value}')

# g)
data_len = len(data)
count_stock_increase = 0
count_stock_increase_follow = 0
last_increase = False
for date, date_data in data.items():
    if date_data['Close']>date_data['Open']:
        count_stock_increase += 1
        if last_increase:
            count_stock_increase_follow += 1
        last_increase = True
    else:
        last_increase = False
print(f'Probability of stock increase {count_stock_increase/data_len}')
# 0.545454

print(f'Probability of subsequently increase {count_stock_increase_follow/count_stock_increase}')
# 0.43478
# So for this limited dataset the theory does not hole True

