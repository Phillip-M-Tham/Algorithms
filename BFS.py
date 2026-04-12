from collections import deque

myMaze= []
mySolution =[]
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
#finds start POS for BFS
def findStartEndPos(theMaze):
    startPos=[];
    endPos=[];
    for row in range(len(theMaze)):
        for col in range(len(theMaze[row])):
            if theMaze[row][col] == 'S':
                startPos=[row,col]
            if theMaze[row][col] =='F':
                endPos=[row,col]
    return startPos,endPos   
            
StartPos,EndPos= findStartEndPos(myMaze)

#in order for BFS to work, we need a queue, a visited set, starting position, and directions(up,down,left,right)
def bfs(theMaze,startingposition):
    queue = deque()
    queue.append((startingposition[0],startingposition[1],[startingposition])) #current row,current col, path
    visited =[]
    while len(queue) > 0: #while queue is not empty run this while loop
        curRow, curCol, path = queue.popleft() #removes beginning item from queue
        if(curRow,curCol) in visited:
            continue #skip this iteration if [CurRow, CurCol] has already been visitied
        visited.append((curRow,curCol)) # add the (CurRow,CurCol) to the visited list
        #goal check
        if theMaze[curRow][curCol] == 'F':
            return path + [(curRow,curCol)]
        #Direction Checks to Update Queue
        #Check above current position (5,5) -> (4,5), check left current position (5,5) -> (5,4), check below current position (5,5)->(6,5), check 
        for deltaRow,deltaCol in [[-1,0],[0,-1],[1,0],[0,1]]:
            tempRow= curRow+deltaRow
            tempCol= curCol+deltaCol
            if(0<= tempRow < len(theMaze) and 0 <= tempCol < len(theMaze[0])):#Boundary check
                if(theMaze[tempRow][tempCol]=='F'):#Goal check
                    return path + [(tempRow,tempCol)]
                if(theMaze[tempRow][tempCol]=='0'):#valid spot check
                    if(tempRow,tempCol) not in visited:#Did we already visit tempSpot in visit check
                        queue.append((tempRow,tempCol,path+[(tempRow,tempCol)]))#updates queue with temp queue if not already visited location 
    #we could not find a valid solution
    return None

def generateSolution(theMaze,theSolution):
    print("Generating Solution")
    mazeCopy=[]
    #get a copy of the the maze
    for row in theMaze:
        copyRow=[]
        for col in row:
            copyRow.append(col)
        mazeCopy.append(copyRow)
    for row,column in theSolution:
        if mazeCopy[row][column] not in ('S','F'):
            mazeCopy[row][column]="x"
    printMaze(mazeCopy)
    
mySolution=bfs(myMaze,StartPos)
print("=====================================================================")
print(mySolution)
print(f"total steps {len(mySolution)}")
generateSolution(myMaze,mySolution)