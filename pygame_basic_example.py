import sys, pygame


pygame.init()  # initialize
width, height = 320, 240  # units in pixels
screen = pygame.display.set_mode((width, height)) # is the background

# create a ball with the below properties
position = [100, 100]  # x, y coordinates
speed = [0.05, 0.01]  # speeed is usually
black = 0, 0, 0  # R,G,B  -- the amount of Red, the amount of Green, the amount of Blue
red = 200, 0, 0

while True:   # infinite loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
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

    pygame.display.update()