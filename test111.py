
word="..m,l..al\*"

word = (word.lower().replace(',',' ').replace('.',' ').replace('\' ',' ').replace('"',' ').replace('*',' ').replace('?',' ').replace('!',' ').replace(';',' ').
        replace(':',' '))

print(word)