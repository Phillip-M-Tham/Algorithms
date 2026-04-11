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
   5. Check above of current location:
      1. Set temp location to above. (5,5)->(4,5). 
      2. Check if temp location is still in bounds(temp row >=0).
      3. Conduct goal check with temp location.
         1. Update path with temp location.
         2. Return valid path.
      4. Check if temp location is a valid empty spot in the maze (0).
      5. Check if temp location is not already in visited list.
      6. Add temp location to the queue to be processed.
         1. Updates path with temp location.    
   6. Check left of current location:
      1. Set temp location to left. (5,5)->(5,4).
      2. Check if temp loaction is still in bounds(temp col >=0).
      3. Conduct goal check with temp location.
         1. Update path with temp location.
         2. Return valid path. 
      4. Check if temp location is a valid empty spot in the maze (0).
      5. Check if temp location is not already in visited list.
      6. Add temp location to the queue to be processed.
         1. Updates path with temp location.  
   7. Check below of current location:
      1. Set temp location the below. (5,5)->(6,5).
      2. Check if temp location is still in bounds(temp row < total rows of maze).
      3. Conduct goal check with temp location.
         1. Update path with temp location.
         2. Return valid path. 
      4. Check if temp location is a valid empty spot in the maze (0).
      5. Check if temp location is not already in visited list.
      6. Add temp location to the queue to be processed.
         1. Updates path with temp location.
   8. Check right of current location:
      1. Set temp location to the right. (5,5)->(5,6).
      2. Check if temp locaiton is still in bounds(temp column < total columns of maze).
      3. Conduct goal check with temp location.
         1. Update path with temp location.
         2. Return valid path. 
      4. Check if temp location is a valid empty spot in the maze(0).
      5. Check if temp location is not already in visited list.
      6. Add temp location to the queue to be processed.
         1. Updates path with temp location.
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
   5. Check above of current location:
      1. Set temp location to above. (5,5) -> (4,5).
      2. Check if temp location is still in bounds. (temp row >=0)
      3. Conduct goal check with temp location.
         1. Update path with temp location.
         2. Return valid path.
      4. Check if temp location is a valid spot in the maze(0).
      5. Check if temp location is not already in visited list.
      6. Add temp location to top of stack.
         1. Updates path with temp location.
   6. Check left of current location:
      1. Set temp location to left. (5,5) -> (5,4).
      2. Check if temp location is still in bounds. (temp column >=0)
      3. Conduct goal check with temp location.
         1. Update path with temp location.
         2. Return valid path.
      4. Check if temp location is a valid spot in the maze(0).
      5. Check if temp location is not already in visited list.
      6. Add temp location to top of stack.
         1. Updates path with temp location.
   7. Check below of current location:
      1. Set temp location to below. (5,5) -> (6,5).
      2. Check if temp location is still in bounds. (temp row < total rows of maze).
      3. Conduct goal check with temp location.
         1. Update path with temp location.
         2. Return valid path.
      4. Check if temp location is a valid spot in the maze(0).
      5. Check if temp location is not already in visited list.
      6. Add temp location to top of stack.
         1. Updates path with temp location.
   8. Check right of current location:
      1. Set temp location to right. (5,5) -> (5,6).
      2. Check if temp location is still in bounds. (temp column >= total columns of maze).
      3. Conduct goal check with temp location.
         1. Update path with temp location.
         2. Return valid path.
      4. Check if temp location is a valid spot in the maze(0).
      5. Check if temp location is not already in visited list.
      6. Add temp location to top of stack.
         1. Updates path with temp location.
4. Return None if unable to find a valid path. 
### Logic Flow Recursively
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
## Helper Functions
## The Maze
