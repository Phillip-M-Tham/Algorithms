# Alogrithims
This Repo is designed to showcase algorithms solving 2D array ASCII mazes.
## Breadth First Search(BFS)
BFS uses a First in First Out(FIFO) process to explore each spot by layer. This visits all neighbors by layer and finds the shortest path to the goal.
BFS uses a queue to conduct FIFO, a list to track visited spots, and a method to track the valid path. This solution uses a list of lists containing [row][col] coordinates for path and visited trackers. The queue is a list of lists that holds [current row, current column, path].
### Logic Flow
1. Add Starting position to queue.
2. Set visited list to an empty list.
3. While queue is not empty:
   1. Remove first item from the queue, updates current row, current column, and path trackers.
   2. check if current row and current column have already been visited.
      1. Skip this iteration if current row and current column match visited list.
   3. Update the visited list with current row and current column.
   4. Conduct goal check with current row and column coordinates against maze.
      1. update path with current location.
      2. return valid path.
   5. Run a for loop for coordinates up left down and right [-1,0],[0,-1],[1,0],[0,1] represented as [deltaRow,deltaCol].
      1. update temprow and tempcol by adding tempRow to deltaRow and tempCol to deltaCol.
      2. Conduct boundary check with temp location (0 <= tempRow < total rows of maze and 0 <= tempCol < total columns of maze).
          1. Conduct goal check with temp location.
             1. Update path with temp location.
             2. Return valid path.
          2. Check if temp location is a valid spot in the maze (0).
             1. Check if temp location is not already in visited list.
                1. Updates path with temp location.
                2. Updates queue to process temp location.
4. Return None if unable to find a valid path. 
## Depth First Search(DFS)
DFS uses a Last in First Out(LIFO) process to explore max depth for a valid path. A max depth will continue until it hits a condtion that makes the path no longer valid or it finds the goal. This does not find the shortest path. The nature of conducting LIFO allows a natural fit for recursion.
DFS uses a stack to conduct LIFO, a list to track visited spots, and a method to track a valid path. This solution uses a list of lists containing [row][column] coorinates for path and visited trackers. The iterative solution uses a stack that is a list of lists that holds [current row, current column, path]
### Logic Flow Iteratively
1. Add starting position to Stack.
2. Set visited list to empty list.
3. While Stack is not empty:
   1. Pop last item on stack, updates current row, current col, and path.
   2. Check if current row and column have already been visited.
      1. Skip this iteration if current row and column match visited list. 
   3. Update the visited list with current row and current column.
   4. Conduct goal check with current row and current column against maze.
      1. Update path with current row and current column.
      2. Return valid path.
   5. Run a for loop for coordinates up left down and right [-1,0],[0,-1],[1,0],[0,1] represented as [deltaRow,deltaCol].
      1. update temprow and tempcol by adding tempRow to deltaRow and tempCol to deltaCol.
      2. Conduct boundary check with temp location (0 <= tempRow < total rows of maze and 0 <= tempCol < total columns of maze).
          1. Conduct goal check with temp location.
             1. Update path with temp location.
             2. Return valid path.
          2. Check if temp location is a valid spot in the maze (0).
             1. Check if temp location is not already in visited list.
                1. Updates path with temp location.
                2. Updates stack to process temp location.
4. Return None if unable to find a valid path. 
### Logic Flow Recursively
1. Conduct boundary check row lower limit (curRow < 0).
   1. Return None.
2. Conduct boundary check column lower limit (curCol < 0).
   1. Return None.
3. Conduct boundary check row upper limit (curRow >= total rows of the Maze).
   1. Return None.
4. Conduct boundary check column upper limit (curCol >= total columns of the Maze).
   1. Return None.
5. Check if current row and current column is a wall.
   1. Return None.
6. Update path list with current row and current column.
7. Check if current row and current column is the goal location in maze.
   1. Return path list.
8. Check if current row and current column is already in visited list.
   1. Return None.
9. Update visited list with current row and current column.
10. Run a for loop for coordinates up left down and right [-1,0],[0,-1],[1,0],[0,1] represented as [deltaRow,deltaCol].
      1. update temprow and tempcol by adding tempRow to deltaRow and tempCol to deltaCol.
      2.  Set result to DFS passing in theMaze,tempRow,tempCol,path list and visited list as parameters.
          1. if result is not None, a valid path is found.
              1. Return result.

## Dijkstra's Alogorithm
Dijkstra is used to find the lowest cost path in a weighted system. This maze is altered to have weights by randomizing 0,3,4 for valid spots previously represented as only 0. This algorithm uses a priority queue as a heap to process lowest accumulated cost for a valid path. There are two separate trackers, distGrid for minimum distance and prevGrid for path taken, to properly update the heap queue. The heap queue is used to keep items ordered by accumulated total cost which allows only the items with the lowest total cost to be processed first efficiently.
### Logic Flow
1. Set starting cost to 0.
2. Add starting cost and starting position to heap queue.
3. Set trackers for distGrid and prevGrid.
4. while heap queue is not empty.
   1. Remove first item from heap to update current cost, current row, and current column.
   2. Conduct goal check with current row and current column against the Maze.
   3. Run a for loop for coordinates up left down and right [-1,0],[0,-1],[1,0],[0,1] represented as [deltaRow,deltaCol].
      1. update temprow and tempcol by adding tempRow to deltaRow and tempCol to deltaCol.
      2. Conduct boundary check with temp location (0 <= tempRow < total rows of maze and 0 <= tempCol < total columns of maze).
         1. Check if temp location is goal.
            1. Update tempCost with currentCost + 1.
         2. check if temp location is valid spot 0.
            1. Update tempCost with currentCost + 1. 
         3. check if temp location is valid spot 3.
            1. Update tempCost with currentCost + 3. 
         4. check if temp location is valid spot 4.
            1. update tempCost with currentCost +4. 
         5. Skip this iteration if temp location is not a valid spot.
         6. Conduct lowest cost check with current cost against tempCost.
            1. update distGrid with temp location storing tempCost.
            2. update prevGrid with temp location storing current location.
            3. update heapqueue with tempCost and temp location.
5. Return None if unable to find a valid path.      
## Helper Functions and Modules
### Common functions
1. generateMaze: Reads the maze.txt file and creates the 2D array with walls(1) and valid spots(0).
2. printMaze: Iterates through the 2D array printing each value for maze.
3. generateSolution: Updates the maze with path solution using "X" and prints out solution.
4. findStartEndPos: Iterates through the 2d array and looks for start pos represented as "S" character and end pos represented as "F" character. Returns startPos and endPos.
### BFS
#### Modules
1. Uses collections module for deque class.
### DFS
#### Modules
1. Iterative
    1. Uses collections module for deque class.
2. Recursive
### Dijkstra
### Modules
1. Uses the random module.
2. uses the heapq module.
### Functions
1. randomizer: Contains a list for 0,3,4. Randomly returns a value from the list. 
2. scatterWeights: Iterates through the 2D array and for every valid 0 spot, replaces it with a random valid weighted value using randomizer. Returns the updated maze with scattered weights.
4. getCost: Contains a dictionary where keys represent valid spots 0,3,4 and values to represent weight cost 1,3,4.Returns the weight of the valid spot.
5. getGrids: Creates two new grids to represent distance tracker and current path tracker. Iterates throught the the maze to create empty rows to match rows of maze for each grid. Distance tracker is set with "inf" for all valid unvisited spots and -1 for all walls. Path tacker sets None for all spots.  
## The Maze
1. Each algorithm uses the same maze, a 40x60 2D array represented by ASCII characters.
2. Start position is always located at [1,1] and represented by "S", End position is always [39,59] and represented by "F". 
3. For BFS and DFS, 1 is a wall and 0 is a valid path.
4. For Dijkstra, 1 is a wall and 0,3,4 is valid path. The random module is used to iterate through the maze when all valid paths are 0 and is set to randomily put the value 0,3,4 to truly scatter weights producing a different random weighted maze each time.
5. The Maze is held in maze.txt and looks like:
1111111111111111111111111111111111111111111111111111111111111
1S00001000000000000000000001000000000001001001000001000000001
1111001111001111001001111111001111111111001001001001111111001
1000000000000001001001001000001001000000000001001001001001001
1001111111111111111111001001111001111001001111001111001001001
1001001000000001001000000000001000000001001001000001000001001
1001001111001001001001001001001111111111001001001001001001001
1000000000001001000001001001000000000000001000001001001000001
1001111111001001001111111111001111001001111001001111001111001
1000001000001000000001000000001000001000000001001000001000001
1001111111111001111111001001001111111111111111111111001001001
1001000001000000000001001001000000000000001001000000001001001
1111111001111001111111111111001111111001001001001111001111111
1000000000000000000001001000001000001001001000000001001001001
1111111001111111001111001111111001111111001111001001111001001
1000001000000001000001001000000000001000000001001000001000001
1001001001111111001111001001001001111001111111001001001001001
1001000001001001000000000001001001001001001000001001000001001
1001111001001001111001001001111111001111001111001001111001001
1000001000001001000001001001000000001001000000001001000001001
1001001111111001111111111001111001111001001001111001111001111
1001001001000001000000000000000000000000001001000000001001001
1111111001111001001001111001001111111001111001111111111001001
1001000001000001001000001001001000000000001001000000000001001
1001001001001111111111111111001111001001111111001111111111001
1001001000001001001001000000000001001001000000000001000001001
1001001001111001001001111111111001111111001001111111001001001
1000001000000000001000000000001001000001001001000000001000001
1111111111001111001001111001001001001111111111001111111111111
1000000000001001000001000001000000000001000000001001000000001
1111111001111001111111111001111111001001111111001001001001001
1001001000000000001000001001000001001001000001000000001001001
1001001111111001001111001111001111111001111001111001001001111
1001001001000001001000001000000000001000000000001001001001001
1001001001111001001001001001001111001111001001111111111001001
1001001000001001001001001001001000000001001000000000001001001
1001001111001001111001111111001111111001001001001001001001001
1001001001000001000001000001000001000001001001001001001000001
1001001001001111111001001111111111001001001001001001001111001
10000000000010000000000000000000000010000010010010010000000F1
1111111111111111111111111111111111111111111111111111111111111
