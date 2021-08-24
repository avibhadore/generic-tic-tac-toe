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
turn = 1
P1 = True
for x in range(9):
    try:
        inputnum = input("Player, type the number of the space you want to fill.\n")
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
    if (turn % 2 ==0):
        P1= False
        print("It is now P2's turn.")
    elif (turn % 2 == 1):
        P1= True
        print("It is now P1's turn.")
#Issues
# turn system doesn't work (e.g. it shouldnt have p1's turn in the last turn)
# not set up for any edgecases at all
# game doesn't identify if anyone won.