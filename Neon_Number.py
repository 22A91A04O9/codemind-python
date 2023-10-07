a=int(input())
s=0
sqr=a*a
while (sqr>0):
    s=s+sqr%10
    sqr=sqr//10
if(a==s):
    print('Neon Number')
else:
    print('Not Neon Number')