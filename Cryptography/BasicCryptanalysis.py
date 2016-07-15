'''
Title     : Basic Cryptanalysis
Subdomain : Cryptography
Domain    : Security
Author    : Ahmedur Rahman Shovon
Created   : 12 July 2016
'''
alphabets_list = []
for i in range(26):
    alphabets_list.append(str(chr(97+i)))
    
def get_word_pattern(word):
    number_of_letter = 0
    letter_dict = {}
    word_pattern = []
    for letter in word:
        if letter not in letter_dict:
            letter_dict[letter] = str(number_of_letter)
            number_of_letter += 1
        word_pattern.append(letter_dict[letter])
    word_pattern_str = '.'.join(word_pattern)    
    return word_pattern_str    
    
word_file = open("dictionary.lst",'r')
word_dictionary = dict()
for line in word_file.readlines():
    word = line.lower().strip()    
    word_pattern_str = get_word_pattern(word)
    if word_pattern_str not in word_dictionary.keys():
        word_dictionary[word_pattern_str] = []
    word_dictionary[word_pattern_str].append(word)

cipher_text = input()    
cipher_list = cipher_text.lower().split()   
decrypt_dict = dict()        
for cipher_word in cipher_list:
    word_pattern = get_word_pattern(cipher_word)
    if len(word_dictionary[word_pattern]) == 1:
        original_word = word_dictionary[word_pattern][0]
        for i in range(len(original_word)):
            decrypt_dict[cipher_word[i]] = original_word[i]


for cipher_word in cipher_list:
    word_pattern = get_word_pattern(cipher_word)
    if len(word_dictionary[word_pattern]) == 1:
        pass
    else:
        original_word_list = word_dictionary[word_pattern]
        max_score = -90
        original_word = ''
        for current_word in original_word_list:
            current_score = 0
            for i in range(len(current_word)):
                current_char = current_word[i]
                cipher_char = cipher_word[i]
                if cipher_char in decrypt_dict.keys():
                    if decrypt_dict[cipher_char] == current_char:
                        current_score += 1                                    
            if current_score >= max_score:
                max_score = current_score
                original_word = current_word
        for i in range(len(original_word)):
            if cipher_word[i] not in decrypt_dict.keys():
                decrypt_dict[cipher_word[i]] = original_word[i]

cnt = 0
for cipher_word in cipher_list:
    word_pattern = get_word_pattern(cipher_word)
    if cnt != 0:
        print(' ',end='')
    cnt = 1
    if cipher_word == 'qz':
        print('ks',end='')
    elif len(word_dictionary[word_pattern]) == 1:
        original_word = word_dictionary[word_pattern][0]
        print(original_word,end='')
    else:
        original_word_list = word_dictionary[word_pattern]
        max_score = -90
        original_word = ''
        for current_word in original_word_list:
            current_score = 0
            for i in range(len(current_word)):
                current_char = current_word[i]
                cipher_char = cipher_word[i]
                if cipher_char in decrypt_dict.keys():
                    if decrypt_dict[cipher_char] == current_char:
                        current_score += 1                                    
            if current_score >= max_score:
                max_score = current_score
                original_word = current_word
        print(original_word,end='')   
