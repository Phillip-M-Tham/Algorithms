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
def findStartPos(theMaze):
    for row in range(len(theMaze)):
        for col in range(len(theMaze[row])):
            if theMaze[row][col] == 'S':
                return (row,col)
            
StartPos= findStartPos(myMaze)

#in order for BFS to work, we need a queue, a visited set, starting position, and directions(up,down,left,right)
def bfs(theMaze,startingposition):
    TotalRows,TotalCols = len(theMaze),len(theMaze[0])

    queue = deque()
    queue.append((startingposition[0],startingposition[1],[startingposition])) #current row,current col, path

    visited =[]

    while len(queue) > 0: #while queue is not empty run this while loop
        CurRow, CurCol, path = queue.popleft() #removes beginning item from queue
        if(CurRow,CurCol) in visited:
            continue #skip this iteration if [CurRow, CurCol] has already been visitied
        
        visited.append((CurRow,CurCol)) # add the (CurRow,CurCol) to the visited list
        
        #goal check
        if theMaze[CurRow][CurCol] == 'F':
            return path + [(CurRow,CurCol)]
        
        #Direction Checks to Update Queue
            #Boundary check
                #DID WE FIND THE SOLUTION CHECK
                #Valid Spot Check
                    #Did We Already visit it check
        #Check above current position (5,5) -> (4,5)
        tempRow = CurRow -1
        tempCol = CurCol
        if(tempRow >= 0): # make sure we are in the maze
            if theMaze[tempRow][tempCol]=='F':
                return path + [(tempRow,tempCol)]
            if theMaze[tempRow][tempCol] == '0': #make sure our projected spot is a viable empty spot
                if(tempRow,tempCol) not in visited: #make sure we are not adding an already visited spot to the queue that processes each node
                    queue.append((tempRow,tempCol,path + [(tempRow,tempCol)]))
        #check left current position (5,5) -> (5,4)
        tempRow = CurRow
        tempCol = CurCol -1
        if(tempCol >= 0):
            if theMaze[tempRow][tempCol]=='F':
                return path + [(tempRow,tempCol)]
            if theMaze[tempRow][tempCol] =='0':
                if(tempRow,tempCol) not in visited:
                    queue.append((tempRow,tempCol,path + [(tempRow,tempCol)]))
        #check bottom current position (5,5) -> (6,5)
        tempRow =CurRow +1
        tempCol =CurCol
        if(tempRow < TotalRows):
            if theMaze[tempRow][tempCol]=='F':
                return path + [(tempRow,tempCol)]
            if theMaze[tempRow][tempCol] =='0':
                if(tempRow,tempCol) not in visited:
                    queue.append((tempRow,tempCol,path + [(tempRow,tempCol)]))
        #check right current position (5,5) -> (5,6)
        tempRow= CurRow
        tempCol =CurCol +1
        if(tempCol < TotalCols):
            if theMaze[tempRow][tempCol]=='F':
                return path + [(tempRow,tempCol)]
            if theMaze[tempRow][tempCol]=='0':
                if(tempRow,tempCol) not in visited:
                    queue.append((tempRow,tempCol,path +[(tempRow,tempCol)]))
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
print(f"total steps {len(mySolution)}")
generateSolution(myMaze,mySolution)