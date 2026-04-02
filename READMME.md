# Alogrithims
This Repo is designed to showcase algorithms solving 2D array ASCII mazes.
## Breadth First Search(BFS)
BFS uses a First in First Out(FIFO) process to explore each spot by layer. This visits all neighbors by layer and finds the shortest path to the goal.
BFS uses a queue to conduct FIFO, a list to track visited spots, and a method to track the valid path. This solution uses a list of lists containing [row][col] coordinates for path and visited trackers.
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
      5. Check if temp location is not already in visited.
      6. Add temp location to the queue to be processed.    
   6. Check left of current location:
      1. Set temp location to left. (5,5)->(5,4).
      2. Check if temp loaction is still in bounds(temp col >=0).
      3. Conduct goal check with temp location.
         1. Update path with temp location.
         2. Return valid path. 
      4. Check if temp location is a valid empty spot in the maze (0).
      5. Check if temp location is not already in visited.
      6. Add temp location to the queue to be processed.  
   7. Check below of current location:
      1. Set temp location the below. (5,5)->(6,5).
      2. Check if temp location is still in bounds(temp row < total rows of maze).
      3. Conduct goal check with temp location.
         1. Update path with temp location.
         2. Return valid path. 
      4. Check if temp location is a valid empty spot in the maze (0).
      5. Check if temp location is not already in visited.
      6. Add temp location to the queue to be processed.
   8. Check right of current location:
      1. Set temp location to the right. (5,5)->(5,6).
      2. Check if temp locaiton is still in bounds(temp column < total columns of maze).
      3. Conduct goal check with temp location.
         1. Update path with temp location.
         2. Return valid path. 
      4. Check if temp location is a valid empty spot in the maze(0).
      5. Check if temp location is not already in visited.
      6. Add temp location to the queue to be processed. 
## Depth First Search(DFS)
DFS uses a Last in First Out(LIFO) process to explore max depth for a valid path. A max depth will continue until it hits a condtion that makes the path no longer valid or it finds the goal. This does not find the shortest path. The nature of conducting LIFO allows a natural fit for recursion.
DFS uses a stack to conduct LIFO, a list to track visited spots, and a method to track a valid path. This solution uses a list of lists containing [row][column] coorinates for path and visited trackers.
## Helper Functions
## The Maze
