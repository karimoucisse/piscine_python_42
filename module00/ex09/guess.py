from random import randint

def main():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit'to end the game")
    print("Good luck!\n")
    num = randint(1, 99)
    count = 1
    while True:
        guess = input("what's your guess between 1 and 99?\n")
        if guess == "exit":
            print("Goodbye!")
            quit()
        if not guess.isdigit():
            print("That's not a number.")
            continue
        if int(guess) == num: 
            if num == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if count == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print(f"Congratulations, you've got it!\nYou won in {count} attempts!")
            quit()
        if(int(guess) > num):
            print("Too high!")
        if(int(guess) < num):
            print("Too low!")
        count +=1
        
if __name__=="__main__":
    main()