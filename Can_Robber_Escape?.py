n=int(input()) 
a=list(map(int,input().split())) 
c=0 
for i in range(n):
    if n<=a[i]:
        c=1
        break
if c==0:
    print("YES")
else:
    print("NO")