def getTimeArray(input_entry):
    time = input(input_entry).split()
    for i in range(len(time)):
        if i%2 == 0:
            if not (int(time[i]) >= 0 and int(time[i]) <= 23):
                print('Error!')
                getTimeArray((input_entry))
        else:
            if not (int(time[i]) >= 0 and int(time[i]) <= 59):
                print('Error!')
                getTimeArray((input_entry))
    time = [int(i) for i in time]
    return time

def addTimeArray(dt,tt):
    train1_hours = dt[0]+tt[0]
    train1_mins = dt[1]+tt[1]
    while train1_mins >= 60:
        train1_hours += 1
        train1_mins -= 60
    train2_hours = dt[2]+tt[2]
    train2_mins = dt[3]+tt[3]
    while train2_mins >= 60:
        train2_hours += 1
        train2_mins -= 60
    print('Arrival Time')
    print(f'{train1_hours}:{train1_mins}')
    print(f'{train2_hours}:{train2_mins}')

dt = getTimeArray('Enter Departure Time:')
tt = getTimeArray('Enter Trip Time:')
addTimeArray(dt, tt)
