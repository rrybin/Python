import random

word_list = ['автобус', 'кран', 'грузовик', 'самосвал', 'пикап', 'манипулятор', 'джип', 'трактор', 'эксковатор']
errors_counter = 0
MAX_ERRORS = 8
def print_list_as_str(arg):
    print(''.join(arg))

secret_word = random.sample(word_list, 1)[0]

#print(secret_word)

users_word = ['*'] * len(secret_word)

print_list_as_str(users_word)

while True:
    letter = input('Введите букву загаданого слова: ').lower()
    if len(letter) != 1 or not letter.isalpha() or not (ord(letter)>=1072 and ord(letter)<=1103):
        continue
    if letter in secret_word:
        for pos, char in enumerate(secret_word):
            if char == letter:
                users_word[pos] = letter
        if ''.join(users_word) == ''.join(secret_word):
            print('Вы выиграли!!!')
            print(f'Загаданное слово: {secret_word}')
            answer = input('Желаете продолжить игру! (Д/Н):' ).upper()
            if answer == 'Д':
                errors_counter = 0
                secret_word = random.sample(word_list, 1)[0]
                users_word = ['*'] * len(secret_word)
                print_list_as_str(users_word)
                continue
            else:        
                break
    else:
        errors_counter += 1
        print(f'Совершено ошибок: {errors_counter}')
        if errors_counter == MAX_ERRORS:
            print('Вы проиграли')
            answer = input('Желаете продолжить игру! (Д/Н):' ).upper()
            if answer == 'Д':
                errors_counter = 0
                secret_word = random.sample(word_list, 1)[0]
                users_word = ['*'] * len(secret_word)
                print_list_as_str(users_word)
                continue
            else:        
                break
    print_list_as_str(users_word)

