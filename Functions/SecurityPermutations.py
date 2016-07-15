'''
Title     : Security Permutations
Subdomain : Functions
Domain    : Security
Author    : Ahmedur Rahman Shovon
Created   : 10 July 2016
'''
n = int(input())
ar = list(map(int,input().split()))
for i in range(n):
    print(ar[ar[i]-1])
