'''
Robot Cleaner

Given a robot cleaner in a room modeled as a grid.
Each cell in the grid can be empty or blocked.
Design an algorithm to clean the entire room using only the 4 given APIs 

Input: 0:blocked 1:access
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
robot start position
row = 1,
col = 3
'''

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot:
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """


def cleanRoom(robot):
    
    # Backtrack, i.e. go back to the previous cell.
    def go_back():
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def backtrack(cell = (0, 0), d = 0):
        visited.add(cell)
        robot.clean()

        # going clockwise
        for i in range(4):
            newDir = (d + i) % 4
            newCell = (cell[0] + directions[newDir][0], \
                        cell[1] + directions[newDir][1])
            
            if not newCell in visited and robot.move():
                backtrack(newCell, newDir)
                go_back()
            
            # turn the robot following your chosen direction : clockwise
            robot.turnRight()

    
    # clockwise directions
    # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    backtrack()
