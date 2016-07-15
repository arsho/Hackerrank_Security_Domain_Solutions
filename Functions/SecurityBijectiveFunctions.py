'''
Title     : Security Bijective Functions
Subdomain : Functions
Domain    : Security
Author    : Ahmedur Rahman Shovon
Created   : 10 July 2016
'''
n = int(input())
ar = list(map(int,input().split()))
set_ar = set(ar)
if len(ar) == len(set_ar):
    print('YES')
else:
    print('NO')
