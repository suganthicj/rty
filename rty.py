x11,y11=map(int,input().split())
l=list(map(int,input().split()))
a=""
for i in range(0,x11-y11):
	a=a+str(l[i])+" "
print(a.strip())
