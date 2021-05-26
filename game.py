""" Number Guessing Game"""
import random  # generates random numbers

list_of_trials = []


def score_board():              #Shows gamer list of attempts in the game
    if len(list_of_trials) <=0:
        print("No score yet.Please play to view your score")
    else:
        print("Your current high score is {} trials.".format(min(list_of_trials)))


def begin_game():
    random_number = int(random.randrange(1, 20))      #range of numbers to be guessed is 1 and 20
    print("Hello gamer!Welcome to the guessing game!")
    gamer_name = input("what is your name?: ")
    start_play = input("Hi, {} would you like to start playing? (Enter yes /no): ".format(gamer_name))
    trys = 0
    score_board()
    while start_play.lower() == "yes":
        try:
            guess = input("Choose a number between 1 and 20: ")
            if int(guess) < 1 or int(guess) > 20:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print("Great! Correct.")      #When guesses the correct value
                trys += 1
                list_of_trials.append(trys)
                print("You have taken {} attempts".format(trys))
                play_again = input("Would you like to play again ?(Enter yes/no): ")
                trys = 5
                score_board()
                random_number = int(random.randrange(1, 20))
                if play_again.lower() == "no":
                    print("Too bad!I wish you could play!")    #prints out when gamer wishes not to play
                    break
            elif int(guess) > random_number:
                print("Not yet there.")
                trys += 1
            elif int(guess) < random_number:
                print("Wow!It is getting higher")
                trys += 1
        except ValueError as err:       #prints out an error if the value is not in the given range
            print("Sorry that is a wrong value.Please try again.")
            print("({})".format(err))
    else:
        print("That's great!Awesome")


    if __gamer_name__ == '__main__':    #begins game when the gamer inputs name
        begin_game()



begin_game()
score_board()