from colorama import Fore
from collections import Counter

target_word = 'ceder'
guess = 'crier'
correct_letters = ''

guess_letter_counts = Counter(guess)
print('guess letter counts: ' + str(guess_letter_counts))
target_letter_counts = Counter(target_word)
print('target letter counts: ' + str(target_letter_counts))

for index, letter in enumerate(guess):
    if letter == target_word[index]:
        correct_letters += letter

correct_letters_counts = Counter(correct_letters)
print('corrects letter counts: ' + str(correct_letters_counts))
print('')

for index, letter in enumerate(guess):
    if letter == target_word[index]:
        print(Fore.GREEN, end='')
        correct_letters_counts[letter] -= 1
    elif letter in target_word:
        num_remaining_target_letters = target_letter_counts[letter] - correct_letters_counts[letter]
        more_remain = num_remaining_target_letters > 0
        if letter in correct_letters and more_remain:
            print(Fore.YELLOW, end='')
        elif letter not in correct_letters:
            print(Fore.YELLOW, end='')

        guess_letter_counts[letter] -= 1

    print(letter + Fore.RESET, end=' ')
    print(letter, index, target_word[index], guess_letter_counts[letter], correct_letters_counts)