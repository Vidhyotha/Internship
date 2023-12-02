n=int(input('Enter the length of the arrays: '))
x=[]
y=[]
z=[]
for i in range(n):
    el=int(input('Enter next element of x '))
    x.append(el)
for j in range(n):
    el=int(input('Enter next element of y '))
    y.append(el)
for k in range(n):
    z.append(x[k]+y[k])
print(z)