gameBoard = list(range(1, 10))


def printBoard(gameBoard):
    print("-------------")
    for i in range(3):
        print("|", gameBoard[0 + i * 3], "|", gameBoard[1 + i * 3], "|", gameBoard[2 + i * 3], "|")
        print("-------------")


def enterValue(userEntry):
    isCont = False
    while not isCont:
        tempAnswer = int(input("Enter your number player " + userEntry+"\n"))
        if tempAnswer in range(1, 10):
            if str(gameBoard[tempAnswer - 1]) not in "X0":
                gameBoard[tempAnswer - 1] = userEntry
                isCont = True
            else:
                print("Invalid entry , this place is taken by another player")


def checkWinner(gameBoard):
    statWinner = ((0, 1, 2), (0, 4, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (2, 4, 6), (3, 4, 5), (6, 7, 8))
    for i in statWinner:
        if gameBoard[i[0]] == gameBoard[i[1]] == gameBoard[i[2]]:
            return gameBoard[i[0]]
    return False


def main(gameBoard):
    count = 0
    isWon = False
    while not isWon:
        printBoard(gameBoard)
        if count % 2 == 0:
            enterValue("X")
        else:
            enterValue("0")
        count += 1
        if count > 4:
            n = checkWinner(gameBoard)
            if n:
                print(n, "WON")
                isWon = True
                break
        if count == 9:
            print("Majority Draw")
            break
    printBoard(gameBoard)


if __name__ == '__main__':
    main(gameBoard)
