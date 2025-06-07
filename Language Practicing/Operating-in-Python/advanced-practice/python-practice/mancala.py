def get_player():
    player = input("Enter Players name: ")
    return player

def take_turn(player, cups):
    print(f"{player}, it's your turn!")
    while True:
        try:
            cup_index = int(input("Choose a cup (0-5): "))
            if 0 <= cup_index <= 5 and cups[cup_index] > 0:
                return cup_index
            else:
                print("Invalid move! Choose a non-empty cup.")
        except ValueError:
            print("Invalid input! Please enter a valid cup number.")

BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '


def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
    
    board = [[SPACE for _ in range((BLOCK_WIDTH + 1) * (len(top_cups) + 2) + 1)] for _ in range(BLOCK_HEIGHT * 2 + 3)]
    for p in range(len(board)):
        board[p][0] = BLOCK_SEP
        board[p][len(board[0]) - 1] = BLOCK_SEP

    for q in range(len(board[0])):
        board[0][q] = BLOCK_SEP
        board[len(board) - 1][q] = BLOCK_SEP

    # draw midline
    for p in range(BLOCK_WIDTH + 1, (BLOCK_WIDTH + 1) * (len(top_cups) + 1) + 1):
        board[BLOCK_HEIGHT + 1][p] = BLOCK_SEP

    for i in range(len(top_cups)):
        for p in range(len(board)):
            board[p][(1 + i) * (1 + BLOCK_WIDTH)] = BLOCK_SEP

    for p in range(len(board)):
        board[p][1 + BLOCK_WIDTH] = BLOCK_SEP
        board[p][len(board[0]) - BLOCK_WIDTH - 2] = BLOCK_SEP

    for i in range(len(top_cups)):
        draw_block(board, i, 0, top_cups[i])
        draw_block(board, i, 1, bottom_cups[i])

    draw_mancala(0, mancala_a, board)
    draw_mancala(1, mancala_b, board)

    print('\n'.join([''.join(board[i]) for i in range(len(board))]))



def draw_mancala(fore_or_aft, mancala_data, the_board):

    if fore_or_aft == 0:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][1 + j] = data[j]
    else:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][len(the_board[0]) - BLOCK_WIDTH - 1 + j] = data[j]


def draw_block(the_board, pos_x, pos_y, block_data):

    for i in range(BLOCK_HEIGHT):
        data = block_data[i][0:BLOCK_WIDTH].rjust(BLOCK_WIDTH)
        for j in range(BLOCK_WIDTH):
            the_board[1 + pos_y * (BLOCK_HEIGHT + 1) + i][1 + (pos_x + 1) * (BLOCK_WIDTH + 1) + j] = data[j]


def run_game():
    top_cups = [4] * 6
    bottom_cups = [4] * 6
    mancala_a = [""] * 5
    mancala_b = [""] * 5

    player1 = get_player()
    player2 = get_player()

    current_player = player1

    while True:
        if current_player == player1:
            cup_index = take_turn(player1, top_cups)
            cups = top_cups
            mancala = mancala_a
        else:
            cup_index = take_turn(player2, bottom_cups)
            cups = bottom_cups
            mancala = mancala_b

        stones = cups[cup_index]
        cups[cup_index] = 0

        while stones > 0:
            cup_index = (cup_index + 1) % 6
            cups[cup_index] += 1
            stones -= 1

        if stones == 0 and cups[cup_index] == 1:
            opposite_cup_index = 5 - cup_index
            mancala[current_player == player1] += bottom_cups[opposite_cup_index] + 1
            bottom_cups[opposite_cup_index] = 0
            cups[cup_index] = 0

        if current_player == player1:
            top_cups = cups
            mancala_a = mancala
            current_player = player2
        else:
            bottom_cups = cups
            mancala_b = mancala
            current_player = player1

        draw_mancala(top_cups, bottom_cups, mancala_a, mancala_b)
        input("Press Enter to continue")

        if sum(top_cups) == 0 or sum(bottom_cups) == 0:
            print("Game Over!")
            draw_mancala(top_cups, bottom_cups, mancala_a, mancala_b)

            if mancala_a[-1] > mancala_b[-1]:
                print(f"{player1} wins!")
            elif mancala_b[-1] > mancala_a[-1]:
                print(f"{player2} wins!")
            else:
                print("It's a tie!")


if __name__ == "__main__":
    run_game()
