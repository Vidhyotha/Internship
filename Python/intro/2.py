list1=[[0,1,2,3],[3,4,5,5],[6,7,8,8],[9,0,1,9]]
maxi=list1[0][0]
mini=list1[0][0]
maxr=[]
minr=[]
maxc=[]
minc=[]
column=[]
for row in list1:
    maxr.append(max(row))
    minr.append(min(row))
    for element in row:
        if (element>maxi):
            maxi=element
        if (element<mini):
            mini=element

for i in range(len(list1)):
    column=[]
    for j in range(len(list1[i])):
        colist=list1[j][i]
        column+=[colist]
    maxc.append(max(column))
    minc.append(min(column))

print("Max: ",maxi)
print("Min: ",mini)
print("Col Wise Min: ",minc)
print("Col Wise Max: ",maxc)
print("Row Wise Max: ",maxr)
print("Row Wise Min: ",minr)