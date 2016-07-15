'''
Title     : Security - Message Space and Ciphertext Space
Subdomain : Terminology and Concepts
Domain    : Security
Author    : Ahmedur Rahman Shovon
Created   : 11 July 2016
'''
m = input()
for i in m:
    x = int(i)
    res = 0
    if x!=9:
        res = x+1
    print(res,end='')
