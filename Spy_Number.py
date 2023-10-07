a=int(input())
sm=0
pro=1
while(a!=0):
    r=a%10
    sm=sm+r
    pro=pro*r
    a=a//10
    
if(sm==pro):
    print('Spy Number')
else:
    print('Not Spy Number')