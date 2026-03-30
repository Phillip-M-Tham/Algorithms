myMaze= []
def generateMaze(theMaze):
    with open("maze.txt", "r") as file:
        for line in file:
            row=list(line.strip())
            theMaze.append(row)
    return theMaze
myMaze= generateMaze(myMaze)
#function to print out the generated maze
def printMaze(theMaze):
    for row in theMaze:
        for cell in row:
            print(cell, end="")
        print();

printMaze(myMaze)#test for printing out the maze

def findStartPos(theMaze):
    for row in range(len(theMaze)):
        for col in range(len(theMaze[row])):
            if theMaze[row][col] == 'S':
                return (row,col)
            
StartPos= findStartPos(myMaze)
print(StartPos)