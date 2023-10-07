a=int(input())
b=int(input())
for i in range(a,b+1):
    m=i
    c=0
    s=0
    while(m!=0):
        rem=m%10
        m=m//10
        c+=1
        if rem==0:
            break
        elif(i%rem==0):
            s+=1
    if s==c:
       print(i,end=' ')