pattern=[]
n=int(input('Enter number of lines: '))
for i in range(n):
    line=[]
    for j in range(i+1):
        if j==0 or j==i:
            line.append(1)
        else:
            line.append(pattern[i-1][j-1]+pattern[i-1][j])
    pattern.append(line)

for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for j in range(i+1):
        print(pattern[i][j],end=' ')
    print()