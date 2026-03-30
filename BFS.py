myMaze= []
def generateMaze(theMaze):
    with open("maze.txt", "r") as file:
        for line in file:
            row=list(line.strip())
            theMaze.append(row)
    return theMaze
myMaze= generateMaze(myMaze)
#print(myMaze)
def printMaze(theMaze):
    for row in theMaze:
        for cell in row:
            print(cell, end="")
        print();
printMaze(myMaze)