from collections import deque

myMaze =[]
def generateMaze(theMaze):
    with open("maze.txt","r") as file:#swap this out to a different maze.txt when ready
        for line in file:
            row=list(line.strip())
            theMaze.append(row)
        return theMaze
myMaze=generateMaze(myMaze)

def printMaze(theMaze):
    for row in theMaze:
        for cell in row:
            print(cell, end="")
        print(" ")

printMaze(myMaze)