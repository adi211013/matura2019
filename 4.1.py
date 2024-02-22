import math
file=open("liczby.txt","r")
numbers=[]
for line in file:
    numbers.append(int(line))
file.close()
counter=0
for x in numbers:
    for i in range(0,12):
        if x==math.pow(3,i):
            counter+=1
            break
print(counter)