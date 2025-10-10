def match_word(word):
    ctr = 0
    lst = []
    for letter in  word:
        if len(letter) > 1 and letter[0]==letter[-1]:
            lst.append(letter)
            ctr += 1
    print(lst)
    return ctr
count = match_word(['aio','cfc','aeiou','xyz'])
print("the number of words", count)    