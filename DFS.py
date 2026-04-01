from collections import deque

myMaze =[]
mySolution=[]
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

def findStartPos(theMaze):
    for row in range(len(theMaze)):
        for col in range(len(theMaze[0])):
            if theMaze[row][col]=="S":
                return [row,col]
            
def findFinishPos(theMaze):
    for row in range(len(theMaze)):
        for col in range(len(theMaze[0])):
            if theMaze[row][col]=="F":
                return [row,col]
            
startPos=findStartPos(myMaze)
endPos=findFinishPos(myMaze)
print(startPos)
print(endPos)

def dfs(myMaze,startPos):
    totalRows,totalCols= len(myMaze), len(myMaze[0])
    stack = deque()
    stack.append((startPos[0],startPos[1],[startPos]))

    visited=[]

    while(len(stack) >0):
        #pop last item from stack
        curRow,curCol,path =stack.pop()
        #if current position already visited skip this iteration
        if(curRow,curCol) in visited:
            continue
        #if curPos is not in visited add curPos to visited
        visited.append((curRow,curCol))

        #if we find goal return path
        if myMaze[curRow][curCol]=="F":
            return path +[(curRow,curCol)]
        #check neighbors
        #check up (5,5) -> (4,5)
        tempRow = curRow -1
        tempCol = curCol
        if(tempRow >= 0):
            if(myMaze[tempRow][tempCol]=="F"):
                return path+[(tempRow,tempCol)]
            if(myMaze[tempRow][tempCol]=="0"):
                if (tempRow,tempCol) not in visited:
                    stack.append((tempRow,tempCol,path+[(tempRow,tempCol)]))
        #check left (5,5) ->(5,4)
        tempRow=curRow
        tempCol=curCol-1
        if(tempCol >=0):
            if(myMaze[tempRow][tempCol]=="F"):
                return path+[(tempRow,tempCol)]
            if(myMaze[tempRow][tempCol]=="0"):
                if (tempRow,tempCol) not in visited:
                    stack.append((tempRow,tempCol,path+[(tempRow,tempCol)]))
        #check down (5,5) -> (6,5)
        tempRow=curRow+1
        tempCol=curCol
        if(tempRow <totalRows):
            if(myMaze[tempRow][tempCol]=="F"):
                return path+[(tempRow,tempCol)]
            if(myMaze[tempRow][tempCol]=="0"):
                if (tempRow,tempCol) not in visited:
                    stack.append((tempRow,tempCol,path+[(tempRow,tempCol)]))
        #check right (5,5) -> (5,6)
        tempRow=curRow
        tempCol=curCol+1
        if(tempCol <totalCols):
            if(myMaze[tempRow][tempCol]=="F"):
                return path+[(tempRow,tempCol)]
            if(myMaze[tempRow][tempCol]=="0"):
                if (tempRow,tempCol) not in visited:
                    stack.append((tempRow,tempCol,path+[(tempRow,tempCol)]))
    #could not find a valid path
    return None

mySolution=dfs(myMaze,startPos)
print(mySolution)