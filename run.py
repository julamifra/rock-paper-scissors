
# class Dashboard:
#     '''
#     Dashboard class. It sets the initial dashboard by choosing the rounds number
#     and manage the elements (rock, paper, scissors) display
#     '''

# 	# scores = {"computer": 0, "player": 0}

#     def __init__(self, rounds, player_name):
#         self.rounds = rounds
#         self.player_name = player_name
        
#     def print(self, element):
#         print(f"Paiting... {element}")


def get_rounds():
    rounds = 0

    while True:
        rounds = input('Please enter a number of rounds (max. 15): ')
    
        if validate_round_number(rounds):
            print(f"Number of rounds: {rounds}")
            break

    return rounds


def validate_round_number(number_value):
    '''
    It validates whether the parameter is a number or not, and if the number is greater than 15
    '''
    try:
        num = int(number_value)
        if num > 15:
            raise ValueError(f"The number of rounds must be less than 15. You set {num}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True


def main():
    '''
    Inialize the game to start playing.
    Run all program functions
    '''
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


main()

