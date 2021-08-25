#ok make tic tac toe
board = {
    "1": "1","2": "2","3": "3",
    "4": "4","5": "5","6": "6",
    "7":"7", "8":"8", "9": "9"
}
def printboard(board):
    print(board["1"]+ "|" + board["2"]+ "|"+ board["3"])
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
printboard(board)
win = False
def checkwin():
    if board["1"]==board["2"]==board["3"]:   #top horizontal win 
        print(playerturn+" wins!")
        x = True
        return x
    if board["4"]==board["5"]==board["6"]: # mid horizontal
        print(playerturn + " wins!")
        x = True
        return x
    if board["7"]==board["8"]==board["9"]: # bot horizontal
        print(playerturn + " wins!")
        x = True
        return x
    if board["1"]==board["4"]==board["7"]:  #left vertical
        print(playerturn + " wins!")
        x = True
        return x
    if board["2"]==board["5"]==board["8"]:  #mid vertical
        print(playerturn + " wins!")
        x = True
        return x
    if board["3"]==board["6"]==board["9"]: #right vertical
        print(playerturn + " wins!")
        x = True
        return x
    if board["1"]==board["5"]==board["9"]:  #diagonal down
        print(playerturn + " wins!")
        x = True
        return x
    if board["3"]==board["5"]==board["7"]:  #diagonal up
        print(playerturn + " wins!")
        x = True
        return x
##################### Game Starts Here ######################################################
turn = 1
P1 = True

for z in range(9):
    try:
        inputnum = input("Player, type the number of the space you want to fill.\n:")
        if P1==True:
            board[inputnum.strip()]="X"
            turn += 1
        else:
            board[inputnum.strip()]="O"
            turn += 1
    except:
        print("Please only input a valid number spot.")   #this code never runs...
        continue
    printboard(board)

    checkwin()
    win = checkwin()
    if win:
        break
    if (turn % 2 ==0):
        P1= False
        print("It is now P2's turn.")
    elif (turn % 2 == 1):   #the "and win == False" parts for these two turn % things was causing it to never change players in the game.
        P1= True
        print("It is now P1's turn.")
    if P1 == True:
        playerturn = "P1"
    else:
        playerturn = "P2"
print("GAME END.")
# Theory for why It says "P1 wins" twice: the win value 
