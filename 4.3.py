def nwd(a,b):
    if b>0:
        return nwd(b,a%b)
    return a
file=open("liczby.txt","r")
numbers=[]
for line in file:
    numbers.append(int(line))
file.close()
firstnumber=0
sequencelength=0
divisor=0
for i in range (0,len(numbers)-1):
    fn=numbers[i]
    sql=1
    j=i+1
    div=nwd(fn,numbers[j])
    while nwd(div,numbers[j])!= 1:
        div = nwd(div, numbers[j])
        sql+=1
        j+=1
    if sql>sequencelength:
        sequencelength=sql
        firstnumber=fn
        divisor=div
print(firstnumber)
print(sequencelength)
print(divisor)
