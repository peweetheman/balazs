from random_word import RandomWords
r = RandomWords()
# Return a single random word
random_word = r.get_random_word()


# print out number of lives remaining and the current word with underscores
num_lives = 6
letters_guessed = []  # a set() would be better since a set keeps only unique elements
while num_lives != 0:
    print('Number of lives remaining: ', num_lives)
    current_word = ''
    for character in random_word:
        if character in letters_guessed:
            current_word += character
        else:
            current_word += '_'
    print(current_word)

    if '_' not in current_word:
        print('You won!')
        break

    guess = input("Guess a letter: ")
    if guess in letters_guessed:
        print('You already guessed that letter!')
    elif guess in random_word:
        print("Good guess!")
    else:
        print("Bad Guess!")
        num_lives = num_lives - 1

    letters_guessed.append(guess)
    print('---------------------------------\n')
