def runGame():
    print("Hello and welcome to Tic-Tac-Toe, a two person game, in which the goal is to line up a row, column or diagonal of the same symbol!")
    #Describing the game#
    
    end=False
    listx=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    #Setting up the tic tac toe board#

    x=1
    while end!=True and x<=10:
    #Repeats until someone has won or 9 turns have been completed#

        print(listx[0:3])
        print(listx[3:6])
        print(listx[6:9])
        #Printing the tic tac toe board#1

        if listx[0]=='X' and listx[1]=='X' and listx[2]=='X':
            print("\n\nGame Over! Congratulations Player 2 on winning!")
            end=True 
        elif listx[0]=='O' and listx[1]=='O' and listx[2]=='O':
            print("\n\nGame Over! Congratulations Player 1 on winning!")
            end=True 
        elif listx[3]=='X' and listx[4]=='X' and listx[5]=='X':
            print("\n\nGame Over! Congratulations Player 2 on winning!")
            end=True 
        elif listx[3]=='O' and listx[4]=='O' and listx[5]=='O':
            print("\n\nGame Over! Congratulations Player 1 on winning!")
            end=True 
        elif listx[6]=='X' and listx[7]=='X' and listx[8]=='X':
            print("\n\nGame Over! Congratulations Player 2 on winning!")
            end=True 
        elif listx[6]=='O' and listx[7]=='O' and listx[8]=='O':
            print("\n\nGame Over! Congratulations Player 1 on winning!")
            end=True 
        elif listx[0]=='X' and listx[3]=='X' and listx[6]=='X':
            print("\n\nGame Over! Congratulations Player 2 on winning!")
            end=True 
        elif listx[0]=='O' and listx[3]=='O' and listx[6]=='O':
            print("\n\nGame Over! Congratulations Player 1 on winning!")
            end=True 
        elif listx[1]=='X' and listx[4]=='X' and listx[7]=='X':
            print("\n\nGame Over! Congratulations Player 2 on winning!")
            end=True 
        elif listx[1]=='O' and listx[4]=='O' and listx[7]=='O':
            print("\n\nGame Over! Congratulations Player 1 on winning!")
            end=True 
        elif listx[2]=='X' and listx[5]=='X' and listx[8]=='X':
            print("\n\nGame Over! Congratulations Player 2 on winning!")
            end=True 
        elif listx[2]=='O' and listx[5]=='O' and listx[8]=='O':
            print("\n\nGame Over! Congratulations Player 1 on winning!")
            end=True 
        elif listx[0]=='X' and listx[4]=='X' and listx[8]=='X':
            print("\n\nGame Over! Congratulations Player 2 on winning!")
            end=True 
        elif listx[0]=='O' and listx[4]=='O' and listx[8]=='O':
            print("\n\nGame Over! Congratulations Player 1 on winning!")
            end=True 
        elif listx[2]=='X' and listx[4]=='X' and listx[6]=='X':
            print("\n\nGame Over! Congratulations Player 2 on winning!")
            end=True 
        elif listx[2]=='O' and listx[4]=='O' and listx[6]=='O':
            print("\n\nGame Over! Congratulations Player 1 on winning!")
            end=True 
            #Checks all possible win conditions#
            #Prints gameover after win condition is met#

        if x%2==0 and end!=True:
            pos=int(input("\nPlayer 2: What position do you want to go in?"))
            #Getting user's input for a position during an even turn#
            if pos in range(1,10):
                if listx[pos-1]=='O' or listx[pos-1]=='X':
                    print("Invalid Position")
                    #if there is already an X or O in the position they want to go in, send an error message#
                else:
                    listx[pos-1]='X'
                    #if it's an even turn, use "X"#
                    x+=1
            else:
                print("Invalid Input")

        elif x%2!=0 and end!=True:
            pos=int(input("\nPlayer 1: What position do you want to go in?"))
            #Getting user's input for a position during an odd turn#
            if pos in range(1,10):
                if listx[pos-1]=='O' or listx[pos-1]=='X':
                    print("Invalid Position")
                    #if there is already an X or O in the position they want to go in, send an error message#
                else:
                    listx[pos-1]='O'
                    #if it's an odd turn, use "O"#
                    x+=1
            else:
                print("Invalid Input")

    Again=str(input("Do you want to play again?"))
    #Asking if they want to play again#
    if Again=='yes' or Again=='Yes':
        runGame()

runGame()
