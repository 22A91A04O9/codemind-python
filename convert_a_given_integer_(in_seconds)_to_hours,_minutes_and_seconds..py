n=int(input())
H=n/3600
M=((n%3600)/60)
S=((n%3600)%60)
print("H:M:S-%d:%d:%d"%(H,M,S))