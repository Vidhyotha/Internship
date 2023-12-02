n=int(input('Enter the length of the list: '))
lst=[]
for i in range(n):
    element=int(input('Enter element: '))
    lst.append(element)
sum=0
for i in lst:
    sum+=i
print(sum)