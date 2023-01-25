import sys, pygame
from random_word import RandomWords
r = RandomWords()
# Return a single random word
random_word = r.get_random_word()


pygame.init()  # initialize
width, height = 320, 240  # units in pixels
screen = pygame.display.set_mode((width, height)) # is the background

# create a ball with the below properties
position = [100, 100]  # x, y coordinates
speed = [0.05, 0.01]  # speeed is usually
black = 0, 0, 0  # R,G,B  -- the amount of Red, the amount of Green, the amount of Blue
red = 200, 0, 0
letters_guessed = []
num_lives = 6
base_font = pygame.font.Font(None, 40)

while True:   # infinite loop
    letter_guessed = ""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                letter_guessed = ""
            else:
                letter_guessed = event.unicode

    if letter_guessed == "":
        pass
    elif letter_guessed in letters_guessed:
        print('You already guessed that letter!')
    else:
        if letter_guessed in random_word:
            print('Good Guess!')
        else:
            print('Bad Guess!')
            num_lives = num_lives - 1

    screen.fill(black)

    # draw the letter guessed on screen
    text_surface = base_font.render(letter_guessed, True, red)
    screen.blit(text_surface, (50, 50))

    # draw the word with blanks on screen
    current_word = ''
    for character in random_word:
        if character in letters_guessed:
            current_word += character
        else:
            current_word += '_'


    # draw the hangman stand
    pygame.draw.line(screen, color=red, start_pos=(0, 10), end_pos=(20,10), width=2)
    pygame.draw.line(screen, color=red, start_pos=(10, 10), end_pos=(10, 80), width=2)
    pygame.draw.line(screen, color=red, start_pos=(10, 80), end_pos=(60, 80), width=2)
    pygame.draw.line(screen, color=red, start_pos=(10, 70), end_pos=(20, 80), width=2)
    pygame.draw.line(screen, color=red, start_pos=(60, 80), end_pos=(60,70), width=2)

    # draw the hangman person
    if num_lives < 6:
        pygame.draw.circle(screen, color=red, center=(61, 65), radius=5)
    if num_lives < 5:
        pygame.draw.line(screen, color=red, start_pos=(60, 60), end_pos=(60,40), width=2)
    if num_lives < 4:
        pygame.draw.line(screen, color=red, start_pos=(60, 40), end_pos=(50,20), width=2)
    if num_lives < 3:
        pygame.draw.line(screen, color=red, start_pos=(60, 40), end_pos=(70,20), width=2)
    if num_lives < 2:
        pygame.draw.line(screen, color=red, start_pos=(60, 60), end_pos=(50,45), width=2)
    if num_lives < 1:
        pygame.draw.line(screen, color=red, start_pos=(60, 60), end_pos=(70,45), width=2)
    if num_lives == 0:
        print("you lost!")
        break


    screen.blit(pygame.transform.flip(screen, flip_x=False, flip_y=True), (0, 0))
    pygame.draw.circle(screen, color=red, center=position, radius=5)
    position[0] = position[0] + speed[0]
    position[1] = position[1] + speed[1]

    # make the ball bounce of the edge of the screen
    if position[1] > height:
        speed[1] = - speed[1]
    # make the ball bounce off of the top of the screen
    if position[1] < 0:
        speed[1] = - speed[1]  # abs(-5) = 5 or abs(5) = 5
    # make the ball bounce off the left and right of the screen
    if position[0] < 0:  # bounce off of left side
        speed[0] = -speed[0]
    if position[0] > width: # check if it went past the right side
        speed[0] = -speed[0]

    pygame.display.flip()