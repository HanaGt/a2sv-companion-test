R=lambda:map(int,input().split())
n,k=R()
a=*R(),
print(sum(sorted(y-x for x,y in zip(a,a[1:]))[:n-k]))