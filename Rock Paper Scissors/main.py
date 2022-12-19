import random


def get_choices():
    player_choice = input("Enter a choice: Rock, Paper, or Scissors\n")
    possible_choices_for_computer = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(possible_choices_for_computer)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}.")

    if player == computer:
        return("It's a tie!")

    elif player == "Rock":
        if computer == "Scissors":
            return("Rock smashes scissors! You win!")
        else:
            return("Paper covers rock! You lose!")

    elif player == "Paper":
        if computer == "Scissors":
            return("Scissors cut paper! You lose!")
        else:
            return("Paper covers rock! You win!")

    elif player == "Scissors":
        if computer == "Rock":
            return("Rock smashes scissors! You lose!")
        else:
            return("Scissors cut paper! You win!")

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)