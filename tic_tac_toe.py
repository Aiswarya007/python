from random import randrange


def display_board(board):
    for i in range(3):
        print("+-------+-------+-------+")
        for j in range(1):
            print("|       |       |       |")
            print("|  ", board[i][0], "  | ", board[i][1], "   | ", board[i][2], "   |")
            print("|       |       |       |")

    print("+-------+-------+-------+")


def status(board):
    si = []
    ci = 0
    sj = []
    cj = 0

    sui = []
    ui = 0
    suj = []
    uj = 0
    c = 0
    cd = 0
    for i in range(len(board)):
        for j in range(len(board)):

            # if board[i][j] == 'X' and board[i][j] == 'O':
            #     print("Tie")
            #     return False

            if board[i][j] == 'X':
                si.append(i)
                ci = si.count(i)

                sj.append(j)
                cj = sj.count(j)
                if i == 0 and j == 2:
                    c += 1
                if i == 2 and j == 0:
                    c += 1
                if i == 0 and j == 0:
                    cd += 1
                if i == 2 and j == 2:
                    cd += 1

            elif board[i][j] == 'O':
                sui.append(i)
                ui = sui.count(i)

                suj.append(j)
                uj = suj.count(j)

            elif board[i][j] != 'X' and board[i][j] != 'O':
                return True

            if ci == 3 or cj == 3:
                print("Computer wins!")
                return False
            elif cd == 2:
                print("Computer wins!")
                return False
            elif ui == 3 or uj == 3:
                print("You win!")
                return False
    print("Tie")
    return False


def enter_move(board):
    for i in range(len(board)):
        for j in range(len(board)):
            board[1][1] = 'X'

    display_board(board)
    user_used = []
    comp_used = []
    occupied = []
    first = [5]
    occupied = first

    while status(board):
        user = int(input("Enter your move: "))

        comp = randrange(1, 10)
        print("comp before while----", comp)
        if user not in user_used:
            user_used.append(user)

        while comp in occupied or comp in user_used:
            comp = randrange(1, 10)

        print("comp----", comp)
        if comp not in comp_used:
            comp_used.append(comp)

        occupied = first + user_used + comp_used
        print("occupied", occupied)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == user:
                    board[i][j] = 'O'

                if board[i][j] == comp:
                    board[i][j] = 'X'

        display_board(board)


board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

enter_move(board)
