import random
from time import sleep


def login():
    tries = 0
    while tries < 3:
        print("Login To Play Guess The Number.")
        username = str(input("Please Enter Your Username Here : "))
        password = str(input("Please Enter Your Password Here : "))
        if username == ("hightechgizmo1") and password == ("********"):
            print("Correct Data... Processing Information... Fetching Game...")
            return True
        else:
            print("Incorrect Credentials, Try Again")
            tries = tries + 1
    print("System Is Closing In 3 Seconds... 3... 2... 1...")
    sleep(3)
    return False

def start_game():
        print("Hello, Welcome To... Guess The Number!!!")
        if login():
            number = random.randint(1, 20)
            chances = 0

            print("Guess The Number In Between 0 And 20")
            while chances < 5:
                guess = int(input("Guess The Number... "))
                if guess == number:
                    chances = chances + 1
                    print(f"The Number You Guessed Is : {guess} and... Congrats! Right Number!!!")
                    break


                elif guess < number:
                    print("The Number You Guessed Is Wrong. Try A Higher Number.  ")



                else:
                    print("Too High! Lower Number Please.")


                if not chances < 5:
                    print("Sorry, You Lost And There Are No Tries Left. Try Again Next Time!")

start_game()
