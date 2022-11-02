grid = [["_","_","_",],
        ["_","_","_",],
        ["_","_","_",]]

# X is Bot move
# O is Human move

def checkWin():

        if (grid[0][0] == grid[0][1] and grid[0][0] == grid[0][2] and grid[0][0] != "_"):
            print("Bot Win") if grid[0][0] == "X" else print("Human Win")
            return True
        elif (grid[1][0] == grid[1][1] and grid[1][0] == grid[1][2] and grid[1][0] != "_"):
            print("Bot Win") if grid[1][0] == "X" else print("Human Win")
            return True
        elif (grid[2][0] == grid[2][1] and grid[2][0] == grid[2][2] and grid[2][0] != "_"):
            print("Bot Win") if grid[2][0] == "X" else print("Human Win")
            return True
        elif (grid[0][0] == grid[1][0] and grid[0][0] == grid[2][0] and grid[0][0] != "_"):
            print("Bot Win") if grid[0][0] == "X" else print("Human Win")
            return True
        elif (grid[0][1] == grid[1][1] and grid[0][1] == grid[2][1] and grid[0][1] != "_"):
            print("Bot Win") if grid[0][1] == "X" else print("Human Win")
            return True
        elif (grid[0][2] == grid[1][2] and grid[0][2] == grid[2][2] and grid[0][2] != "_"):
            print("Bot Win") if grid[0][2] == "X" else print("Human Win")
            return True
        elif (grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2] and grid[0][0] != "_"):
            print("Bot Win") if grid[0][0] == "X" else print("Human Win")
            return True
        elif (grid[2][0] == grid[1][1] and grid[2][0] == grid[0][2] and grid[2][0] != "_"):
            print("Bot Win") if grid[2][0] == "X" else print("Human Win")
            return True
        else:
            return False

def checkSignWin(sign):

        if (grid[0][0] == grid[0][1] and grid[0][0] == grid[0][2] and grid[0][0] == sign):
            return True
        elif (grid[1][0] == grid[1][1] and grid[1][0] == grid[1][2] and grid[1][0] == sign):
            return True
        elif (grid[2][0] == grid[2][1] and grid[2][0] == grid[2][2] and grid[2][0] == sign):
            return True
        elif (grid[0][0] == grid[1][0] and grid[0][0] == grid[2][0] and grid[0][0] == sign):
            return True
        elif (grid[0][1] == grid[1][1] and grid[0][1] == grid[2][1] and grid[0][1] == sign):
            return True
        elif (grid[0][2] == grid[1][2] and grid[0][2] == grid[2][2] and grid[0][2] == sign):
            return True
        elif (grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2] and grid[0][0] == sign):
            return True
        elif (grid[2][0] == grid[1][1] and grid[2][0] == grid[0][2] and grid[2][0] == sign):
            return True
        else:
            return False

def checkDraw():
    for row in grid:
        for cell in row:
            if cell == "_":
                return False
    print("Draw")
    return True

def turn(x, y, sign):
    if(grid[x][y] == "O" or grid[x][y] == "X"):
        print("Invalid Move.")
    else:
        grid[x][y] = sign

def minimax(grid, maximizing):
    if (checkSignWin("X")):
        return 1
    elif(checkSignWin("O")):
        return -1
    elif(checkDraw()):
        return 0    

    if(maximizing):
        bestScore = -200
        for x in range(3):
            for y in range(3):
                if grid[x][y] == "_":
                    grid[x][y] = "X"
                    score = minimax(grid, False)
                    grid[x][y] = "_"
                    if(score > bestScore):
                        bestScore = score
        return bestScore
    else:
        bestScore = 200
        for x in range(3):
            for y in range(3):
                if grid[x][y] == "_":
                    grid[x][y] == "O"
                    score = minimax(grid, True)
                    grid[x][y] = "_"
                    if(score < bestScore):
                        bestScore = score
        return bestScore


def AI():
    bestScore = -2
    bestX = 0
    bestY = 0
    for x in range(3):
        for y in range(3):
            if grid[x][y] == "_":
                grid[x][y] = "X"
                score = minimax(grid, False)
                grid[x][y] = "_"
                if(score > bestScore):
                    bestScore = score
                    bestX = x
                    bestY = y
    print(bestX, bestY)
    turn(bestX, bestY, "X")

while not checkWin() and not checkDraw():
    x = int(input("Enter X value: "))
    y = int(input("Enter Y value: "))
    turn(x, y, "O")
    AI()
    for row in grid:
        print(row)
