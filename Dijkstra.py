myMaze=[]
mySolution=[]
def generateMaze(theMaze):
    with open("./maze.txt","r") as file:
        for line in file:
            row = list(line.strip())
            theMaze.append(row)
        return theMaze
def printMaze(theMaze):
    for row in range(len(theMaze)):
        for col in range(len(theMaze[0])):
            print(theMaze[row][col],end="")
        print(" ")
myMaze=generateMaze(myMaze)
printMaze(myMaze)