'''
Title     : Security Function Inverses
Subdomain : Functions
Domain    : Security
Author    : Ahmedur Rahman Shovon
Created   : 10 July 2016
'''
n = int(input())
ar = list(map(int,input().split()))
pos = []
for i in range(1,n+1):
    pos.append(i)
z = zip(ar,pos)
z = sorted(z,key=lambda x:x[0])
for t in z:
    print(t[1])
