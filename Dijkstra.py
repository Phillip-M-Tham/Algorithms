import random

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

#Randomizer
def randomizer():
    options=["0","3","4"]
    return random.choice(options);
#Modify default maze to scatter wieghts
def scatterWeights(theMaze):
    for row in range(len(theMaze)):
        for col in range(len(theMaze[0])):
            if (theMaze[row][col]=="0"):
                randomWeight=randomizer()
                theMaze[row][col]=randomWeight
    return theMaze
myMaze=scatterWeights(myMaze)
printMaze(myMaze)