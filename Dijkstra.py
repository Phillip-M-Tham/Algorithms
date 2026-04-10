import random
import heapq

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

def findStartPos(theMaze):
    for row in range(len(theMaze)):
        for col in range(len(theMaze[0])):
            if(theMaze[row][col] =="S"):
                return [row,col]
#calculates cost of cell value passed
def getCost(value):
    costs= {
        0:1,
        3:3,
        4:4
    }
    return costs.get(value,None)


def dijkstra(theMaze,startPos):
    currentCost=0
    heapqueue=[]
    heapq.heappush(heapqueue,(currentCost,startPos[0],startPos[1]))

#update maze to get scattered weights
myMaze=scatterWeights(myMaze)
printMaze(myMaze)