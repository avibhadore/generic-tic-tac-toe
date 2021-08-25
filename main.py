#ok make tic tac toe
board = {
    "1": "1","2": "2","3": "3",
    "4": "4","5": "5","6": "6",
    "7":"7", "8":"8", "9": "9"
}
def printboard(board):      #i dont know if this parameter actually does anything
    print(board["1"]+ "|" + board["2"]+ "|"+ board["3"])
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
printboard(board)
win = False
def checkwin():
    if board["1"]==board["2"]==board["3"]:   #top horizontal win
        win = True                                                 #win == True only happens within the function. Then it becomes
        return print(playerturn+"wins!")
    if board["4"]==board["5"]==board["6"]: # mid horizontal
        win = True
        return print(playerturn + "wins!")
    if board["7"]==board["8"]==board["9"]: # bot horizontal
        win = True
        return print(playerturn + "wins!")
    if board["1"]==board["4"]==board["7"]:  #left vertical
        win = True
        return print(playerturn + "wins!")
    if board["2"]==board["5"]==board["8"]:  #mid vertical
        win = True
        return print(playerturn + "wins!")
    if board["3"]==board["6"]==board["9"]: #right vertical
        win = True
        return print(playerturn + "wins!")
    if board["1"]==board["5"]==board["9"]:  #diagonal down
        win = True
        return print(playerturn + "wins!")
    if board["3"]==board["5"]==board["7"]:  #diagonal up
        win = True
        return print(playerturn + "wins!")
##################### Game Starts Here ######################################################
turn = 1
P1 = True

for x in range(9):
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
    if win:  #THIS NEVER GETS RUN
        break
    if (turn % 2 ==0) and win == False:
        P1= False
        print("It is now P2's turn.")
    elif (turn % 2 == 1) and win == False:
        P1= True
        print("It is now P1's turn.")
    if P1 == True:
        playerturn = "P1"
    else:
        playerturn= "P2"
print("Hooray, we reached the end of the code without breaking everything!")
