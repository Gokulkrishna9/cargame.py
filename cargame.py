#car game

help = "Start - To start the car \n Stop - To stop the car \n Quit - To quit the game"
a = "The car has started, Now you're ready to go..."
b = "You've stopped the car :("
c = "You've ended the game" 
i = 0

while i<=20:
    Guess = str(input(">")).lower
    i = i+1
    
    if Guess == "start":
        print(a)
    elif Guess == "stop":
        print(b)
    elif Guess == "quit":
        break
    elif Guess == "help":
        print(help)
    else:
        print("I don't understand that ! :-(")
