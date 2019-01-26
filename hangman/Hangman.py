#Hangman Game
import json
import random
print("Select Category:")
print("1. Animal")
print("2. Sport")
print("3. Bathroom")
b = ''
while(b !='1' and b!= '2' and b !='3'):
    b = input('input(1-3) : ')

file_open = "Catalog_" + b + ".json"
data_random = random.randrange(5)
wrong = 10
score = 0
true_word = 0
with open(file_open) as json_file:  
    data = json.load(json_file)
    print("Hint : ",data['word'][data_random]['hint'])
    word = data['word'][data_random]['words']
    word = word.lower()
    wrong_word = ''
    word_show = ''
    for i in word:
        if (i >= '0' and i<= '9') or i == ' ' :    
            word_show += i +' '
            true_word += 1
        else:
            word_show += '_ '
    print(word_show,'score ',score,', remaining wrong guess ',wrong)
    while((true_word != len(word)) and wrong != 0):
        hang = ''
        isWord = True
        while(len(hang) != 1):
            hang = input()
            hang = hang.lower()
        for i in range(len(word)):
            if word[i] == hang:
                score += 10
                true_word += 1
                isWord = False
                cout =0
                mem = list(word_show)
                mem[i*2] = word[i]
                word_show = "".join(mem)
        if isWord:
            wrong -= 1
            wrong_word += hang
            score -= 5
        if (len(wrong_word) == 0):
            print(word_show,'score ',score,', remaining wrong guess ',wrong)
        else:
            print(word_show,'score ',score,', remaining wrong guess ',wrong, ', wrong guessed : ',wrong_word)
        


            
    