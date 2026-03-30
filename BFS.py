from collections import deque

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
#finds start POS for BFS
def findStartPos(theMaze):
    for row in range(len(theMaze)):
        for col in range(len(theMaze[row])):
            if theMaze[row][col] == 'S':
                return (row,col)
            
StartPos= findStartPos(myMaze)
print(StartPos)

#in order for BFS to work, we need a queue, a visited set, starting position, and directions(up,down,left,right)
def bfs(theMaze,startingposition):
    rows,cols = len(theMaze),len(theMaze[0])

    queue = deque()
    queue.append((startingposition[0],startingposition[1],[])) #current row,current col, path

    visited =[]

    while len(queue) > 0: #while queue is not empty run this while loop
        CurRow, CurCol, path = queue.popleft() #removes beginning item from queue
        if(CurRow,CurCol) in visited:
            continue #skip this iteration if CurRow, CurCol has already been visitied
        else:
            visited.append(CurRow,CurCol)