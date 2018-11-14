import random
def name_to_number(name):
    if name == "rock":
        return int(0)
    if name == "Spock":
        return int(1)
    if name == "paper":
        return int(2)
    if name == "lizard":
        return int(3)
    if name == "scissors":
        return int(4)
    else:
        print("Invalid input")
        exit


def number_to_name(number):
    if number == 0:
        return "rock"
    if number == 1:
        return "Spock"
    if number == 2:
        return "paper"
    if number == 3:
        return "lizard"
    if number == 4:
        return "scissors"
    else:
        print("Invalid input")
        exit
    

def rpsls(player_choice):
    print ("Player chose"), player_choice
    player = name_to_number(player_choice)
    computer = random.randrange(0,4)
    print ("Computer chose"), number_to_name(computer)
    result = (player - computer) % 5
    if (result == 1) or (result == 2):
        print ("Player wins!")
    elif player == computer:
        print ("It's a tie!")
    else:
        print ("Computer wins!")
