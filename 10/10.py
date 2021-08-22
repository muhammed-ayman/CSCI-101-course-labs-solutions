"""
[{'city': 'alex', 'temp':50}, {'city': 'cairo', 'temp':60}]
"""
TempList=[]
n = int(input('enter no. of cities'))
for i in range(n):
    tempDict={}
    cityname=input('city name:') #read city name
    t=float(input('temperature:')) #read temperature
    tempDict['city']=cityname #add the cityname and temperature to a dict.
    tempDict['temp']=t
    TempList.append(tempDict) #add the dict to the list
print(TempList)
