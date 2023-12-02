for i in range(1000,9999):
    num=str(i)
    flag1=(int(num[0])+int(num[1])+int(num[2])+int(num[3]))==12
    flag2=(int(num[2])==(abs(int(num[0])-int(num[1]))))
    flag3=(int(num[3])==(int(num[0])+int(num[2])))
    if (flag1 and flag2 and flag3):
        print(i)
