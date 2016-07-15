'''
Title     : Security Involution
Subdomain : Functions
Domain    : Security
Author    : Ahmedur Rahman Shovon
Created   : 10 July 2016
'''
n = int(input())
ar = list(map(int,input().split()))
chk = True
for i in range(n):
    if ar[ar[i]-1]!=(i+1):
        chk = False
        break
if chk == True:
    print('YES')
else:
    print('NO')
