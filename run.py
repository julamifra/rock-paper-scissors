
# class Game:
#     """
#     Dashboard class. It sets the initial dashboard by choosing the rounds number
#     and manage the elements (rock, paper, scissors) display
#     """

#     scores = {"computer": 0, "player": 0}

#     def __init__(self, rounds, player_name):
#         self.rounds = rounds
#         self.player_name = player_name
        
#     def print(self, element):
#         print(f"Painting... {element}")


    
# class Round:

#     def __init__(self):




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
        elif rounds > 15:
            print(f"The number of rounds must be less than 15. You set {rounds}")
        else:
            print(f"Number of rounds: {rounds}")
            break
        
    return rounds


# --------------------------
# -- Validation functions --
# --------------------------


def validate_element(element):
    allowed_elements = ["r", "p", "s", "R", "P", "S"]

    if element in allowed_elements:
        print("sdfg")



# --------------------------
# ----- Main functions -----
# --------------------------

# def play(game):
#     """
#     """
#     print(game.scores)


#     while True:
#         print('Choose one element to play: R(rock), P(paper) or S(scissor)')
#         element = player_element = input('Select an element: ')

#         if validate_element(element):
#             print(f"Number of rounds: {rounds}")
#             break

#     return rounds


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

    # game = Game(rounds, player_name)



main()

