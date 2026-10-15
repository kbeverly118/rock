"""
rps.py

Redistributed and modified with permission from the
EECS Department at The University of Michigan, Ann Arbor

Name: Kayden Beverly

CS 104: Project 2
FALL 2026

Description: A simple two-player Rock, Paper, Scissors game for the terminal. Players play three rounds, and the game announces the winner.
"""



"""
rps.py

CS 104: Project 2
FALL 2026

Description: A two-player Rock, Paper, Scissors game.
Players play three rounds, and the game announces the winner.
"""

COURSE_NAME = "CS 104"
MAX_ROUNDS = 3

ROCK = "r"
PAPER = "p"
SCISSORS = "s"
DEFAULT_MOVE = ROCK

PLAYER_1 = 1
PLAYER_2 = 2
DEFAULT_NAME_1 = "Connor"
DEFAULT_NAME_2 = "M'gann"

DRAW = 0

ERROR_NAME = 1
ERROR_MOVE = 2

PLAY_RPS = 1
PLAY_RPSLS = 2
QUIT_CHOICE = 3


def is_move_good(move):
    """Return True if the move is rock, paper, or scissors."""
    if len(move) != 1:
        return False

    move = move.lower()
    return move == ROCK or move == PAPER or move == SCISSORS


def is_round_winner(move, opponent_move):
    """Return True if the first move beats the second move."""
    move = move.lower()
    opponent_move = opponent_move.lower()

    return (
        (move == ROCK and opponent_move == SCISSORS)
        or (move == SCISSORS and opponent_move == PAPER)
        or (move == PAPER and opponent_move == ROCK)
    )


def get_name(player_number):
    """Get a player's name or use the default if it is empty."""
    if player_number == PLAYER_1:
        name = input("Player 1, enter your name: ")
        if name.strip() == "":
            print_error_message(ERROR_NAME)
            return DEFAULT_NAME_1
    else:
        name = input("Player 2, enter your name: ")
        if name.strip() == "":
            print_error_message(ERROR_NAME)
            return DEFAULT_NAME_2

    return name


def get_menu_choice():
    """Display the menu until the user enters a valid choice."""
    while True:
        print_menu()
        choice = input("Choice --> ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid menu choice")
            continue

        if (
            choice == PLAY_RPS
            or choice == PLAY_RPSLS
            or choice == QUIT_CHOICE
        ):
            return choice

        print("Invalid menu choice")


def get_move(player_name):
    """Get a player's move or use rock if the move is invalid."""
    move = input(player_name + ", enter your move: ")

    if not is_move_good(move):
        print_error_message(ERROR_MOVE)
        return DEFAULT_MOVE

    return move.lower()


def announce_round_winner(winner_name):
    """Print the round winner or announce a draw."""
    if winner_name == "":
        print("This round is a draw!")
    else:
        print(winner_name + " wins the round!")


def do_round(p1_name, p2_name):
    """Play one round and return the winning player's number."""
    p1_move = get_move(p1_name)
    p2_move = get_move(p2_name)

    if p1_move == p2_move:
        return DRAW

    if is_round_winner(p1_move, p2_move):
        return PLAYER_1

    return PLAYER_2


def announce_winner(winner_name):
    """Print the overall game winner or announce no winner."""
    if winner_name == "":
        print("No winner!")
    else:
        print("Congratulations " + winner_name + "!")
        print("You won " + COURSE_NAME + " Rock, Paper, Scissors!")


def do_game(p1_name, p2_name, game_type):
    """Play three rounds and return the overall winner's name."""
    if game_type == PLAY_RPSLS:
        print("Under Construction")
        return ""

    p1_wins = 0
    p2_wins = 0

    for _ in range(MAX_ROUNDS):
        round_winner = do_round(p1_name, p2_name)

        if round_winner == PLAYER_1:
            p1_wins += 1
            announce_round_winner(p1_name)
        elif round_winner == PLAYER_2:
            p2_wins += 1
            announce_round_winner(p2_name)
        else:
            announce_round_winner("")

    if p1_wins > p2_wins:
        return p1_name

    if p2_wins > p1_wins:
        return p2_name

    return ""


def rps():
    """Run the Rock, Paper, Scissors game."""
    print_initial_header()

    p1_name = get_name(PLAYER_1)
    p2_name = get_name(PLAYER_2)

    while True:
        choice = get_menu_choice()

        if choice == QUIT_CHOICE:
            break

        winner_name = do_game(p1_name, p2_name, choice)
        announce_winner(winner_name)

    print_closer()
