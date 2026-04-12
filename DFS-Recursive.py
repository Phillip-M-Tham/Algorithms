myMaze=[]
mySolution=[]
visited=[]
path=[]
def generateMaze(theMaze):
    with open("maze.txt","r") as file:
        for line in file:
            row=list(line.strip())
            theMaze.append(row)
        return theMaze
myMaze=generateMaze(myMaze)
def printMaze(theMaze):
    for row in range(len(theMaze)):
        for col in range(len(theMaze[row])):
            print(theMaze[row][col], end="")
        print(" ")
printMaze(myMaze)

def findStartEndPos(theMaze):
    startPos=[]
    endPos=[]
    for row in range(len(theMaze)):
        for col in range(len(theMaze[row])):
            if(theMaze[row][col]=="S"):
                startPos= [row,col]
            if(theMaze[row][col]=="F"):
                endPos=[row,col]
    return startPos,endPos
startPos,endPos=findStartEndPos(myMaze)
print(startPos)
print(endPos)
def dfs(theMaze,curRow,curCol,path,visited):
    
    #out of bounds checks
    if(curRow < 0 ):
        return None
    if(curCol < 0):
        return None
    if(curRow >= len(theMaze)):
        return None
    if(curCol >= len(theMaze[0])):
        return None
    #wall check
    if(theMaze[curRow][curCol]=="1"):
        return None
    #update path
    path=path + [(curRow,curCol)]
    #goal check
    if(theMaze[curRow][curCol]=="F"):
        return path
    #already visited check
    if (curRow,curCol) in visited:
        return None
    #add current spot to visited
    visited.append((curRow,curCol))
    #conduct neighbor check
    for deltaRow,deltaCol in [[-1,0],[0,-1],[1,0],[0,1]]:
        tempRow=curRow +deltaRow
        tempCol=curCol +deltaCol
        result=dfs(theMaze,tempRow,tempCol,path,visited)
        if result is not None:
            return result
        
def generateSolution(theMaze,theSolution):
    for row in range(len(theMaze)):
        for col in range(len(theMaze[0])):
            if(theMaze[row][col]!= "S" or theMaze[row][col]!= "F"):
                if (row,col) in theSolution:
                    theMaze[row][col]="X"
    printMaze(theMaze)
    

mySolution=dfs(myMaze,startPos[0],startPos[1],path,visited)
print(mySolution)
print(f"total steps is {len(mySolution)}")
generateSolution(myMaze,mySolution)