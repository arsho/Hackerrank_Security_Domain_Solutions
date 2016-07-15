'''
Title     : Security Key Spaces
Subdomain : Terminology and Concepts
Domain    : Security
Author    : Ahmedur Rahman Shovon
Created   : 11 July 2016
'''
m = input()
k = int(input())
for i in m:
    x = int(i)
    print((x+k)%10,end='')
