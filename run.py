"""
Import random library
"""
import random

ALLOWED_ELEMENTS = ["r", "p", "s", "R", "P", "S"]


class Game:
    """
    Dashboard class. It sets the initial dashboard by choosing the number
    of rounds, the player name.
    It contains functions to increment the current round and the score
    """

    def __init__(self, player_name, rounds):
        self.player_name = player_name
        self.rounds = rounds
        self.current_round = 1
        self.score = {"computer": 0, "player": 0}

    def increment_current_round(self):
        """
        Increment by one the current number of rounds
        """
        self.current_round = self.current_round + 1

    def increment_score(self, who="computer"):
        """
        Increment the either the player score or the computer score
        """
        self.score[who] = self.score[who] + 1


# -------------------------------
# -------- Get functions --------
# -------------------------------

def get_rounds():
    """
    Get number of rounds input from the user.
    Validate isnumber() and greater than 15.
    Return the number of rounds.

    Returns: It returns the number of rounds the user has entered
    """
    rounds = 0

    while True:
        rounds = input('Please enter a number of rounds (mix: 1, max: 15):\n')

        if not rounds.isnumeric():
            print(f"Invalid input: A number must be entered. You entered: {rounds}")
        elif int(rounds) > 15 or int(rounds) == 0:
            print(f"The number of rounds must be less than 15 and greater than 0. You set {rounds}")
        else:
            print(f"Number of rounds: {rounds}")
            break
    return rounds


def get_random_element():
    """
    Get a random element between Rock, Paper and Scissor
    """
    return random.choice(tuple(ALLOWED_ELEMENTS))


def get_winner(computer_element, player_element):
    """
    Determine the winner of the game by passing the two elements from
    the player and the computer.
    It returns who is the winner or "equal" instead.
    """

    game = (computer_element + player_element).upper()

    if game == "RP" or game == "PS" or game == "SR":
        return "player"
    elif game == "PR" or game == "SP" or game == "RS":
        return "computer"
    else:
        return "equal"


# ---------------------------
# ------ Print functions ------
# ---------------------------

def print_element(element, name):
    """
    It prints out the element and the user name passed as parameter
    """
    if element in ["r", "R"]:
        print(f"{name}: ROCK..........")
        print('---------XXX-----------')
        print('--------X---X----------')
        print('-------X-----X---------')
        print('------X-------X--------')
        print('-------X-----X---------')
        print('--------X---X----------')
        print('---------XXX-----------')
    elif element in ["p", "P"]:
        print(f"{name}: PAPER.........")
        print('--------XXXXXX---------')
        print('--------X----X---------')
        print('--------X----X---------')
        print('--------X----X---------')
        print('--------X----X---------')
        print('--------X----X---------')
        print('--------XXXXXX---------')
    else:
        print(f"{name}: SCISSORS......")
        print('------X-------X--------')
        print('-------X-----X---------')
        print('--------X---X----------')
        print('---------XXX-----------')
        print('-------XX---XX---------')
        print('-------XX---XX---------')
        print('-------XX---XX---------')


def print_final_score(game):
    """
    It prints out the Score of the game (passed as parameter)
    """

    computer_score = game.score['computer']
    player_score = game.score['player']

    print('|||||||||||||||||||||||||||||||')
    print(f"FINAL SCORE -> Computer: {computer_score}, You: {player_score}")
    print(f"{game.player_name if int(player_score) > int(computer_score) else 'Computer'} win!! ")
    print('|||||||||||||||||||||||||||||||')


# --------------------------
# ----- Main functions -----
# --------------------------


def play(game):
    """
    By receieving the game instance as a parameter, this function start
    to play to the game.
    The while loop finishes when it's been iterated the numbers of
    rounds specified in the class attribute.
    Once the loop is done, the print_final_score function is called.
    """

    while int(game.current_round) <= int(game.rounds):
        print('|||||||||||||||||||||||||||||||')
        print(f"SCORE -> Computer: {game.score['computer']}, {game.player_name}: {game.score['player']}")
        print("NEXT ROUND: ", game.current_round)
        print('|||||||||||||||||||||||||||||||')

        print('Choose one element to play: R(rock), P(paper) or S(scissor)')
        player_element = input('Select an element:\n')

        if player_element not in ALLOWED_ELEMENTS:
            print(f"|-|ERROR|-| Invalid character: {player_element}")
        else:
            print_element(player_element, game.player_name)
            computer_element = get_random_element()
            print_element(computer_element, "computer")

            result = get_winner(computer_element, player_element)
            if result == "equal":
                print("Who win? Draw!")
            else:
                print(f"Who win? {'computer' if result == 'computer' else game.player_name }")
                game.increment_score(result)
                game.increment_current_round()

    print_final_score(game)


def main():
    """
    Inialize the game to start playing.
    Run all program functions.
    Here, the users input their name and the number of rounds the want to play
    """
    print('-------------------------------')
    print('Welcome to ROCK-PAPER-SICCORS!!')
    print('In order to play, use the following letter:')
    print('r: rock')
    print('p: paper')
    print('s: scissor')
    print('GOOD LUCK!')
    print('-------------------------------')

    while True:
        try:
            player_name = input('Please enter your name:\n')

            if len(player_name) < 3:
                raise ValueError("At least 3 characteres are required")
            if len(player_name) > 15:
                raise ValueError("Maximum characteres for the username is 15")
            else:
                print("Username: ", player_name)
                break
        except ValueError as err:
            print(f"Invalid data: {err}, please try again.\n")

    rounds = get_rounds()

    game = Game(player_name, rounds)
    print('-------------------------------')
    print(f"Hello {player_name}! Let's start!")
    print('-------------------------------')
    play(game)


main()
