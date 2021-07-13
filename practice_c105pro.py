import csv
import math 
import statistics

with open('data.csv',newline='')as f:
        reader=csv.reader(f)
        fileData=list(reader)

data=fileData[0]

def mean(data):
    numlen=len(data)
    sum=0
    for x in data:
        sum+=int(x)

    mean=sum/numlen
    return mean


squared_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squared_list.append(a)

sum=0
for i in squared_list:
    sum=-sum+i

result=sum/(len(data)-1)
std_dev=math.sqrt(result)
print(std_dev)


