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

def findStartEndPos(theMaze):
    startPos= []
    endPos=[]
    for row in range(len(theMaze)):
        for col in range(len(theMaze[0])):
            if(theMaze[row][col] =="S"):
                startPos= [row,col]
            if(theMaze[row][col] =="F"):
                endPos=[row,col]
    return startPos,endPos
#calculates cost of cell value passed
def getCost(value):
    costs= {
        0:1,
        3:3,
        4:4
    }
    return costs.get(value,None)

def getGrids(theMaze):
    theGrid=[]
    prevGrid=[]
    for row in range(len(theMaze)):
        newRow=[]
        newPrevRow=[]
        for col in range(len(theMaze[0])):
            newRow.append(float("inf"))
            newPrevRow.append(None)
        theGrid.append(newRow)
        prevGrid.append(newPrevRow)
    for row in range(len(theMaze)):
        for col in range(len(theMaze[0])):
            if(theMaze[row][col]=="1"):
                theGrid[row][col]=-1
    return theGrid,prevGrid

def dijkstra(theMaze,startPos):
    startCost=0
    heapqueue=[]
    heapq.heappush(heapqueue,(startCost,startPos[0],startPos[1]))
    distGrid,prevGrid=getGrids(theMaze)
    #set up distGrid
    distGrid[startPos[0]][startPos[1]]=0
    #printMaze(distGrid)
    while(heapqueue):
        currentCost,curRow,curCol=heapq.heappop(heapqueue)
        if(theMaze[curRow][curCol]=="F"):
            return currentCost,prevGrid
        #up [-1,0] left[0,-1] down[1,0] right[0,1]
        for deltaRow,deltaCol in ([-1,0],[0,-1],[1,0],[0,1]):
            tempRow=curRow+deltaRow
            tempCol=curCol+deltaCol
            #boundary check
            if(0 <= tempRow <len(theMaze) and 0<= tempCol < len(theMaze[0])):
                if(theMaze[tempRow][tempCol]=="F"):
                    prevGrid[tempRow][tempCol]=(curRow,curCol)
                    return currentCost, prevGrid
                if(theMaze[tempRow][tempCol]=="0"):
                    tempCost=currentCost+getCost(0)
                elif(theMaze[tempRow][tempCol]=="3"):
                    tempCost=currentCost+getCost(3)
                elif(theMaze[tempRow][tempCol]=="4"):
                    tempCost=currentCost+getCost(4)
                else:
                    continue
                if tempCost < distGrid[tempRow][tempCol]:
                    distGrid[tempRow][tempCol]=tempCost
                    prevGrid[tempRow][tempCol]=(curRow,curCol)
                    heapq.heappush(heapqueue,(tempCost,tempRow,tempCol))
            
def getPath(pathGrid,endPos):
    cur=endPos
    path =[]
    while cur is not None:
        path.append(cur)
        cur=pathGrid[cur[0]][cur[1]]
    path.reverse()
    return path

#update maze to get scattered weights
myMaze=scatterWeights(myMaze)
printMaze(myMaze)
startPos,endPos=findStartEndPos(myMaze)
shortestCost,pathGrid=dijkstra(myMaze,startPos)
print("===================================================")
myPath=getPath(pathGrid,endPos)
print(myPath)