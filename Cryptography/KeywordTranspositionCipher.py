'''
Title     : Keyword Transposition Cipher
Subdomain : Cryptography
Domain    : Security
Author    : Ahmedur Rahman Shovon
Created   : 11 July 2016
'''
import collections
alpha_ar=[]
for i in range(0,26):
    alpha_ar.append(str(chr(65+i)))
n = int(input())
for t in range(n):
    keyword = input()
    cipher = input()
    keyword_mod = []
    for i in keyword:
        if i not in keyword_mod:
            keyword_mod.append(i)
    keyword_mod_len = len(keyword_mod)
    substitution_od = collections.OrderedDict()
    for i in keyword_mod:
        substitution_od[i] = []
    cnt = 0
    pos = 0
    column_ar = keyword_mod
    for i in alpha_ar:
        if i not in keyword_mod:
            column_ar.append(i)
    for i in range(0,keyword_mod_len):
        cnt = i
        key = keyword_mod[pos]
        while (cnt<26):            
            character = column_ar[cnt]
            if key!=character:
                substitution_od[key].append(character)
            cnt += keyword_mod_len
        pos += 1    
    substitution_od = sorted(substitution_od.items())
    substitution_ar = []
    for key_val in substitution_od:
        substitution_ar.append(key_val[0])
        for j in key_val[1]:
            substitution_ar.append(j) 
    decryption_dict = dict(zip(substitution_ar,alpha_ar))
    original_msg = ''
    for c in cipher:
        if c in decryption_dict.keys():
            original_msg += decryption_dict[c]
        else:
            original_msg += c
    print(original_msg)
