grid = [["_","_","_",],
        ["_","_","_",],
        ["_","_","_",]]

# X is Bot move
# O is Human move

def checkWin():

        if (grid[0][0] == grid[0][1] and grid[0][0] == grid[0][2] and grid[0][0] != "_"):
            return True
        elif (grid[1][0] == grid[1][1] and grid[1][0] == grid[1][2] and grid[1][0] != "_"):
            return True
        elif (grid[2][0] == grid[2][1] and grid[2][0] == grid[2][2] and grid[2][0] != "_"):
            return True
        elif (grid[0][0] == grid[1][0] and grid[0][0] == grid[2][0] and grid[0][0] != "_"):
            return True
        elif (grid[0][1] == grid[1][1] and grid[0][1] == grid[2][1] and grid[0][1] != "_"):
            return True
        elif (grid[0][2] == grid[1][2] and grid[0][2] == grid[2][2] and grid[0][2] != "_"):
            return True
        elif (grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2] and grid[0][0] != "_"):
            return True
        elif (grid[2][0] == grid[1][1] and grid[2][0] == grid[0][2] and grid[2][0] != "_"):
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
        print("Human")
        return -1
    elif(checkDraw()):
        print("Draw")
        return 0

    if(maximizing):
        bestScore = -2
        for x in range(2):
            for y in range(2):
                if grid[x][y] == "_":
                    grid[x][y] = "X"
                    score = minimax(grid, False)
                    grid[x][y] = "_"
                    if(score > bestScore):
                        bestScore = score
        return bestScore
    else:
        bestScore = 2
        for x in range(2):
            for y in range(2):
                if grid[x][y] == "_":
                    grid[x][y] == "O"
                    score = minimax(grid, True)
                    grid[x][y] = "_"
                    if(score < bestScore):
                        bestScore = score
        return bestScore


def AI():
    bestScore = -200
    bestMove = [0, 0]
    for x in range(2): 
        for y in range(2):
            if grid[x][y] == "_":
                grid[x][y] = "X"
                score = minimax(grid, False)
                grid[x][y] = "_"
                if(score > bestScore):
                    bestScore = score
                    bestMove = [x, y]
    print(bestMove[0], bestMove[1])
    turn(bestMove[0], bestMove[1], "X")

while not checkWin():
    x = int(input("Enter X value: "))
    y = int(input("Enter Y value: "))
    turn(x, y, "O")
    AI()
    for row in grid:
        print(row)
