dep_time = input('Enter the departure time > ')
arr_time = input('Enter the arrival time > ')

dep_time_h = int(dep_time.split(':')[0])
dep_time_m = int(dep_time.split(':')[1])
arr_time_h = int(arr_time.split(':')[0])
arr_time_m = int(arr_time.split(':')[1])

dep_mis = dep_time_m+dep_time_h*60
arr_mins = arr_time_m+arr_time_h*60
total_time = arr_mins-dep_mis

print(f'Hours: {total_time//60}, Minutes: {total_time%60}')
