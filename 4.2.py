def silnia(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*silnia(n-1)
def rozbij_i_oblicz_silnie(n):
    n=str(n)
    nums=[]
    for x in n:
        nums.append(int(x))
    suma=0
    for x in nums:
        suma+=silnia(x)
    return suma

file=open("liczby.txt","r")
nums=[]
for line in file:
    nums.append(int(line))
file.close()
counter=0
result=[]
for x in nums:
    if x==rozbij_i_oblicz_silnie(x):
        result.append(x)
        counter+=1
print(result)
print(counter)