"""
Description:    This project is to create a Battleship game. Two players will be able to
                place their respective ships on a 9x9 grid and take turns firing shots at each other's fleets, and
                the game code will register shots and when a player has sunk all of their opponent's ships that
                player wins.
"""

# These are the constants that have specific indications on the board
EMPTY = '  '
HIT = 'HH'
MISS = 'MM'
SHIP_NAMES = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2
}


def create_board():  # Creates an empty game board.
    board = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append(EMPTY)
        board.append(row)
    return board


def display_board(board1, board2=None, hide_ships=False):  # Function to display the current player's board
    row_number = 0
    for i in range(len(board1)):
        print(f"    {i}", end="")

    if board2 is not None:
        print("      ", end="")
        for i in range(len(board2[0])):
            print(f"    {i}", end="")
        print(end="")
    else:
        print()

    for row1 in board1:
        if board2 is None:
            print(f"{row_number}  {' | '.join(row1)} |")
        else:
            row2_display = []
            for cell in board2[row_number]:
                if hide_ships and cell != EMPTY and cell != MISS and cell != HIT:
                    row2_display.append("  ")
                else:
                    row2_display.append(cell)
            row2_display_str = ' | '.join(row2_display)
            print(f"{row_number}  {' | '.join(row1)} |                {row_number}  {row2_display_str} |")
        row_number += 1  # Adds row number for the next iteration at beginning


def place_ships(board):  # This function will place the ships on the board
    for ship_name, length in SHIP_NAMES.items():
        placed = False
        while not placed:
            display_board(board)
            coordinates = input(f"Enter x y coordinates to place the {ship_name}: ").split()
            x, y = int(coordinates[0]), int(coordinates[1])
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                print("Coordinates out of bounds. Please enter valid coordinates.")
            else:
                direction = input("Enter Right or Down (r or d): ").lower()
                if valid_placement(board, x, y, direction, length):
                    place_ship(board, x, y, direction, length, ship_name)
                    placed = True
                else:
                    print("Invalid position, Lets try placing the ship again.")


# function to check if a ship can be placed at a given position
def valid_placement(board, starting_row, starting_col, direction, length):
    # This function will check if a ship can be placed at a given position
    if direction == 'r':
        if starting_col + length > 10:
            return False
        for i in range(length):
            if board[starting_row][starting_col + i] != EMPTY:
                return False
    else:
        if starting_row + length > 10:
            return False
        for i in range(length):
            if board[starting_row + i][starting_col] != EMPTY:
                return False
    return True


def place_ship(board, row_index, col_index, direction, length, ship_name):
    if direction == 'r':
        for i in range(length):
            board[row_index][col_index + i] = ship_name[:2]
    else:
        for i in range(length):
            board[row_index + i][col_index] = ship_name[:2]


def register_shot(board, row_pos, col_pos):
    # This function will register a shot on the opponent's board, either being hit or miss.
    if board[row_pos][col_pos] == EMPTY:
        board[row_pos][col_pos] = MISS
        return "miss"
    elif board[row_pos][col_pos] != EMPTY and board[row_pos][col_pos] != HIT and board[row_pos][col_pos] != MISS:
        ship_symbol = board[row_pos][col_pos]
        name = ""
        hits = 0

        if ship_symbol == "Ca":
            name = "Carrier"
            hits = 0
            for i in range(10):
                for j in range(10):
                    if board[i][j] == "Ca" and board[i][j] != EMPTY:
                        hits += 1
        elif ship_symbol == "Ba":
            name = "Battleship"
            hits = 0
            for i in range(10):
                for j in range(10):
                    if board[i][j] == "Ba" and board[i][j] != EMPTY:
                        hits += 1
        elif ship_symbol == "Cr":
            name = "Cruiser"
            hits = 0
            for i in range(10):
                for j in range(10):
                    if board[i][j] == "Cr" and board[i][j] != EMPTY:
                        hits += 1
        elif ship_symbol == "Su":
            name = "Submarine"
            hits = 0
            for i in range(10):
                for j in range(10):
                    if board[i][j] == "Su" and board[i][j] != EMPTY:
                        hits += 1
        elif ship_symbol == "De":
            name = "Destroyer"
            hits = 0
            for i in range(10):
                for j in range(10):
                    if board[i][j] == "De" and board[i][j] != EMPTY:
                        hits += 1

        if hits == SHIP_NAMES.get(ship_symbol, 0):
            for i in range(10):
                for j in range(10):
                    if board[i][j] == ship_symbol:
                        board[i][j] = HIT
            return f"You sunk the {name}"
        else:
            board[row_pos][col_pos] = HIT
            return f"hit the {name}"
    else:
        return "You've fired at this location, Try a different coordinate."


def game_progress(board):
    for row in board:
        for cell in row:
            if cell != EMPTY and cell != HIT and cell != MISS:
                return False
    return True


def run_game():
    player1_board = create_board()
    player2_board = create_board()

    print("Player 1, prepare to place your fleet.")
    place_ships(player1_board)
    print("\nPlayer 2, prepare to place your fleet.")
    place_ships(player2_board)

    running = True
    player1_won = False
    player2_won = False

    while running:
        print("\nPlayer 1's turn:")
        display_board(player1_board, player2_board, hide_ships=True)

        valid_input = False
        while not valid_input:
            coordinates = input("Enter coordinates to shoot (x y): ").split()
            if len(coordinates) != 2:
                print("Invalid input. Please enter valid coordinates.")
            else:
                x = int(coordinates[0])
                y = int(coordinates[1])
                if 0 <= x < len(player2_board) and 0 <= y < len(player2_board[0]):
                    valid_input = True
                else:
                    print("Coordinates out of bounds. Please enter valid coordinates.")

        result = register_shot(player2_board, x, y)
        if result[:3] == "hit":
            print(f"You {result}!")
        elif result == "miss":
            print("You missed the target!")
        elif result == "You've fired at this location, Try a different coordinate.":
            print("Try another target!")

        player1_won = game_progress(player2_board)
        if player1_won:
            print("Player 1 wins!")
            running = False

        # Checks if the game continues after player 1's turn
        if running:
            # Player 2's turn
            print("\nPlayer 2's turn:")
            display_board(player2_board, player1_board, hide_ships=True)

            valid_input = False
            while not valid_input:
                coordinates = input("Enter coordinates to shoot (x y): ").split()
                if len(coordinates) != 2:
                    print("Invalid input. Please enter valid coordinates.")
                else:
                    x = int(coordinates[0])
                    y = int(coordinates[1])
                    if 0 <= x < len(player1_board) and 0 <= y < len(player1_board[0]):
                        valid_input = True
                    else:
                        print("Coordinates out of bounds. Please enter valid coordinates.")

            result = register_shot(player1_board, x, y)
            if result[:3] == "hit":
                print(f"You {result}!")
            elif result == "miss":
                print("This shot was a miss!")
            elif result == "You've fired at this location, Try a different coordinate.":
                print("Try again, choose another coordinate!")

            player2_won = game_progress(player1_board)
            if player2_won:
                print("Player 2 wins!")
                running = False


if __name__ == '__main__':
    run_game()
