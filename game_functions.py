from random import randint


def computer_choice():
    """
    Generate a random choice between three options
    :return: a string "rock" or "paper" or "scissors".
    """
    # Generate a random integer (0-2)
    numran = randint(0, 2)
    # A list containing options.
    opt = ['rock', 'paper', 'scissors']
    # Computer choice.
    cmpch = opt[numran]
    return cmpch


def who_winner(players_wins, computers_wins, games_played):
    """
    Finding out who is the winner and printing the appropriate message, plus some stats, to the console
    :param players_wins: integer representing the number of times the player has won.
    :param computers_wins: integer representing the number of times the player has lost.
    :param games_played: an integer representing the number of games played.
    :return: None
    """
    if computers_wins == players_wins:
        print("It is a Tie")
    elif computers_wins > players_wins:
        print("You loose.")
        print("computer's wins: " + str(computers_wins))
        print("your wins: " + str(players_wins))
    elif computers_wins < players_wins:
        print("Congratulations, you win!")
        print("computer's wins: " + str(computers_wins))
        print("your wins: " + str(players_wins))
    print("Games played: " + str(games_played))


def who_wins_thistime(players_choice, cch):
    """
    Check who is a winner based on the conditions
    :param players_choice: player's choice/move
    :param cch: computer's choice/move
    :return: winner - player/computer
    """

    winner = None
    # Checking whether the player entered an acceptable response.
    options = ['scissors', 's', 'paper', 'p', 'rock', 'r', 'q']
    if players_choice not in options:
        print("Unacceptable response, please choose one of the following: ", end='')
        print(options)

    elif players_choice == 'q':
        return None

    # Conditionals for finding out who is the winner of an individual move.
    elif cch == players_choice:
        print("computer's choice: " + cch)
        print("It's a Tie")
        winner = 'tie'
    elif cch in ['paper', 'p'] and players_choice in ['scissors', 's']:
        print("computer's choice: " + cch)
        print("You win.")
        winner = 'player'
    elif cch in ['scissors', 's'] and players_choice in ['rock', 'r']:
        print("computer's choice: " + cch)
        print("You win")
        winner = 'player'
    elif cch in ['rock', 'r'] and players_choice in ['paper', 'p']:
        print("computer's choice: " + cch)
        print("You win.")
        winner = 'player'
    else:
        print("computer's choice: " + cch)
        print("You lose.")
        winner = 'player'
    return winner
