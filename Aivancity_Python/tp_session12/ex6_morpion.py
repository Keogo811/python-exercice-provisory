"""
Exercise 6: Morpion 3x3 (Tic-Tac-Toe) in console
Goal: Implement a complete 2-player Tic-Tac-Toe game using lists, conditionals, and loops.
"""


def display_board(board):
    """
    Display the 3x3 Tic-Tac-Toe board.
    
    Args:
        board: A list of 9 elements representing the board (positions 1-9)
    """
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def is_winner(board, player):
    """
    Check if the given player has won.
    
    Args:
        board: A list of 9 elements
        player: 'X' or 'O'
        
    Returns:
        True if player has won, False otherwise
    """
    # Define all winning combinations (indices)
    winning_combinations = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal
        [2, 4, 6],  # Anti-diagonal
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    
    return False


def is_board_full(board):
    """
    Check if the board is completely filled.
    
    Args:
        board: A list of 9 elements
        
    Returns:
        True if board is full, False otherwise
    """
    for cell in board:
        if cell == " ":
            return False
    return True


def is_valid_move(board, position):
    """
    Check if a move is valid.
    
    Args:
        board: A list of 9 elements
        position: The position to check (0-8)
        
    Returns:
        True if position is valid and empty, False otherwise
    """
    if position < 0 or position > 8:
        return False
    if board[position] != " ":
        return False
    return True


def get_player_move(board, player):
    """
    Get a valid move from the player.
    
    Args:
        board: A list of 9 elements
        player: 'X' or 'O'
        
    Returns:
        The valid position (0-8) for the player's move
    """
    while True:
        try:
            position_input = input(f"Player {player}, enter position (1-9): ").strip()
            position = int(position_input) - 1  # Convert to 0-8 index
            
            if is_valid_move(board, position):
                return position
            else:
                print("That position is already taken or invalid. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def play_game():
    """
    Main game loop for Tic-Tac-Toe.
    """
    # Initialize the board (empty cells represented by spaces)
    board = [" " for _ in range(9)]
    current_player = "X"
    
    print("=== Tic-Tac-Toe (Morpion 3x3) ===")
    print("Positions are numbered 1-9:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    
    # Game loop
    while True:
        display_board(board)
        
        # Get player move
        position = get_player_move(board, current_player)
        board[position] = current_player
        
        # Check if current player won
        if is_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break
        
        # Check if board is full (draw)
        if is_board_full(board):
            display_board(board)
            print("It's a draw! Game over.")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"


def main():
    """
    Main function to run the game with replay option.
    """
    while True:
        play_game()
        
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
