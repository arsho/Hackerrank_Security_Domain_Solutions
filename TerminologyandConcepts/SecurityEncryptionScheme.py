'''
Title     : Security Encryption Scheme
Subdomain : Terminology and Concepts
Domain    : Security
Author    : Ahmedur Rahman Shovon
Created   : 11 July 2016
'''
def get_factorial(n):
    if n == 1:
        return 1
    return n*get_factorial(n-1)

n = int(input())
print(get_factorial(n))
