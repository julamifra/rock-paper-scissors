import random

ALLOWED_ELEMENTS = ["r", "p", "s", "R", "P", "S"]

class Game:
    """
    Dashboard class. It sets the initial dashboard by choosing the rounds
    number and manage the elements (rock, paper, scissors) display
    """

    def __init__(self, player_name, rounds):
        self.player_name = player_name
        self.rounds = rounds
        self.current_round = 0
        self.score = {"computer": 0, "player": 0}
        
    def increment_current_round(self):
        self.current_round = self.current_round + 1

    def get_current_round(self):
        return self.current_round
    
    def increment_score(self, who = "computer"):
        self.scores[who] = self.scores[who] + 1

    def get_score(self):
        return self.score


# --------------------------
# -------- Otheerrr --------
# --------------------------

def get_rounds():
    """
    Get number of rounds input from the user.
    Validate isnumber() and greater than 15.
    Return the number of rounds.
    """
    rounds = 0

    while True:
        rounds = input('Please enter a number of rounds (max. 15): ')
    
        if not rounds.isnumeric():
            print(f"Invalid input: A number must be entered. You entered: {rounds}")
        elif int(rounds) > 15:
            print(f"The number of rounds must be less than 15. You set {rounds}")
        else:
            print(f"Number of rounds: {rounds}")
            break
        
    return rounds



def get_random_element():
    """
    Get a random element between Rock, Paper and Scissor
    """
    return random.choice(tuple(ALLOWED_ELEMENTS))



# ---------------------------
# ------ Draw function ------
# ---------------------------

def print_element(element, name):
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
        print(f"{name}: SCISSOR.......")
        print('------X-------X--------')
        print('-------X-----X---------')
        print('--------X---X----------')
        print('---------XXX-----------')
        print('-------XX---XX---------')
        print('-------XX---XX---------')
        print('-------XX---XX---------')


# --------------------------
# ----- Main functions -----
# --------------------------

def play(game):
    """

    """
    

    while True:
        print('|||||||||||||||||||||||||||||||')
        print("ROUND: ", game.get_current_round())
        score = game.get_score()
        print(f"SCORE -> Computer: {game.score['computer']}, {game.player_name}: {game.score['player']}")
        print('|||||||||||||||||||||||||||||||')

        print('Choose one element to play: R(rock), P(paper) or S(scissor)')
        player_element = input('Select an element: ')

        if player_element not in ALLOWED_ELEMENTS:
            print(f"|-|ERROR|-| Invalid character: {player_element}")
            # break
        else:
            print_element(player_element, game.player_name)
            game.increment_current_round()
            computer_element = get_random_element()
            print_element(computer_element, "computer")
            





def main():
    """
    Inialize the game to start playing.
    Run all program functions
    """
    print('-------------------------------')
    print('Welcome to ROCK-PAPER-SICCORS!!')
    print('In order to play, use the following letter:')
    print('r: rock')
    print('p: paper')
    print('s: scissor')
    print('GOOD LUCK!')
    print('-------------------------------')

    player_name = input('Please enter your name: ')
    print("Username: ", player_name)
    rounds = get_rounds()

    game = Game(player_name, rounds)
    print('-------------------------------')
    print(f"Hello {player_name}! Let's start!")
    print('-------------------------------')
    play(game)



main()

