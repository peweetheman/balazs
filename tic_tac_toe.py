# 0 <- blank
# 1 <- X
# 2 <- O
list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

turn = 'X'
while True:
    index = int(input(f"Enter player 1 ({turn}'s) index of move: "))
    index = index - 1
    list[index] = turn

    # print out 3x3 grid
    print(list[0:3])
    print(list[3:6])
    print(list[6:9])

    # check all rows
    if list[0] == list[1] == list[2] != " ":
        print("This team won: ", turn)
        break
    if list[3] == list[4] == list[5] != " ":
        print("This team won: ", turn)
        break
    if list[6] == list[7] == list[8] != " ":
        print("This team won: ", turn)
        break

    # check all columns
    if list[0] == list[3] == list[6] != " ":
        print("This team won: ", turn)
        break
    if list[1] == list[4] == list[7] != " ":
        print("This team won: ", turn)
        break
    if list[2] == list[5] == list[8] != " ":
        print("This team won: ", turn)
        break

    # check diaganols
    if list[0] == list[4] == list[8] != " ":
        print("This team won: ", turn)
        break
    if list[2] == list[4] == list[6] != " ":
        print("This team won: ", turn)
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'