"""This is the main file."""
import game_functions as gf


print("What mode do you want to play?"
      "Mode1: you will enter the n number of games from which the winner will be determined. If you have more"
      "wins then the computer after n-games, you win."
      "Mode2: the winner is determined after a single game.")
mode = int(input("Enter 1 for mode1 or 2 for mode 2:"))

if int(mode) == 2:
    q = input("Do you want to play (y/n)?: ")
    while q != 'n':
        games = int(input("How many games are you willing to play before the winner is determined? (enter an integer):"
                          ""))
        # The main loop:
        print('Enter one of the following options: "rock", "paper", "scissors" (or the first letter ex: "r" for '
              '"rock"). Enter "q" to quit whenever you feel like it.')

        # Some stats about a game.
        computers_wins = 0
        players_wins = 0
        games_played = 0

        for game in range(games):
            players_choice = input("Make a choice: ")
            cch = gf.computer_choice()
            if players_choice == 'q':
                break

            # Checking whether the player entered an acceptable response.
            options = ['scissors', 's', 'paper', 'p', 'rock', 'r', 'q']
            if players_choice not in options:
                print("Unacceptable response, please choose one of the following: ", end='')
                print(options)
                players_choice = input("Please make a choice: ")

            # Based on the response, check who is the winner.
            winner = gf.who_wins_thistime(players_choice, cch)
            if winner == 'player':
                players_wins += 1
            elif winner == 'computer':
                computers_wins += 1

            # The flag/breaking point.
            elif winner is None:
                break

            games_played += 1

        # Finding out who is the winner and printing the appropriate message, plus some stats, to the Python console.
        gf.who_winner(players_wins, computers_wins, games_played)

        q = input("Do you want to try another one? (y/n): ")


elif mode == 1:
    games = 0
    wins = 0
    losses = 0
    ties = 0
    q = input("Do you want to play (y/n)?: ")
    print('Enter one of the following options: "rock", "paper", "scissors" (or the first letter ex: "r" for '
          '"rock"). Enter "q" to quit whenever you feel like it.')
    players_choice = input("Make a choice: ")
    comp_choice = gf.computer_choice()
    while players_choice != 'q':
        # The main loop:
        winner = gf.who_wins_thistime(players_choice, comp_choice)
        if winner == 'player':
            wins += 1
        elif winner == 'computer':
            losses += 1
        elif winner == 'tie':
            ties += 1
        players_choice = input("Make another choice: ")
        comp_choice = gf.computer_choice()
        games += 1
    print("games played: " + str(games))
    print("games won: " + str(wins))
    print("games lost: " + str(losses))
    print("ties: " + str(ties))

print("See you later.")
