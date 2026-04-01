myMaze=[]
mySolution=[]
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

def findStartPos(theMaze):
    for row in range(len(theMaze)):
        for col in range(len(theMaze[row])):
            if(theMaze[row][col]=="S"):
                return [row,col]
startPos=findStartPos(myMaze)
print(startPos)
def findFinishPos(theMaze):
    for row in range(len(theMaze)):
        for col in range(len(theMaze[row])):
            if(theMaze[row][col]=="F"):
                return [row,col]
endPos=findFinishPos(myMaze)
print(endPos)
#set path with starting position
path=[[startPos]]

def dfs(curRow,curCol,path){
    
}
