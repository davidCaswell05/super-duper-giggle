import random
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango']
word = random.choice(fruits)
lives = len(word) + 2
guessed = []
while True:
    won = True
    for letter in word:
        if letter in guessed:
            print(letter, end=' ')
        else:
            print('_', end=' ')
            won = False
    print()
    if won:
        print('You won!')
        break
    guess = input('Guess a letter:')
    guessed.append(guess)
    if guess not in word:
        lives -= 1
        print('Wrong! You have', lives, 'lives left')
        if lives == 0:
            print('You lost!')
            break