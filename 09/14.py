def getPositiveArray(input_entry):
    ids = input(input_entry).split()
    for i in ids:
        if int(i) < 0:
            print('Invalid Input!')
            getPositiveArray(input_entry)
    return ids

def computeAverage(wait):
    avg = 0
    for i in wait:
        avg += int(i)

    return avg/len(wait)

def getIdLongWait(id, wait, avg):
    arr = []
    for i in range(len(id)):
        if float(wait[i]) > avg:
            arr.append(int(id[i]))
    return arr

id = getPositiveArray('Enter ID List:')
wait = getPositiveArray('Enter waiting time list: ')
avg = computeAverage(wait)
print('Average waiting time = %.2f\n' % avg)
idLongWait = getIdLongWait(id,wait,avg)
print('IDs for customers who waited longer than average are:')
print(idLongWait)
