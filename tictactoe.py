grid = [["_","_","_",],
        ["_","_","_",],
        ["_","_","_",]]

def turn():
    x = int(input("Enter X value: "))
    y = int(input("Enter Y value: "))
    if(grid[x][y] == "X"):
        print("Invalid Move.")
        turn()
    else:
        grid[x][y] = "X"

while True:
    turn()
    print(grid)
