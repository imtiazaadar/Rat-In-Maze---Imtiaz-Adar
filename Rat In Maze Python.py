 # Imtiaz Adar
 # Rat In Maze
 # Backtracking
 # Date : 27/06/2021
 # Email : imtiaz-adar@hotmail.com, imtiazadarofficial@gmail.com

# Given maze
maze = [

        [1, 0, 1, 1, 0],
        [1, 1, 1, 0, 1],
        [0, 0, 1, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 1, 1, 1, 0]
    
    ]
size = 5 # Size = 5
# Created a new maze for solution and initialized all values by zero
new_maze = [[0 for j in range(size)] for i in range(size)]


# Given maze print
def maze_print():
    print()
    for row in range(size):
        for col in range(size):
            print(maze[row][col], end=' ')
        print()
    print()

# Solved maze print
def new_maze_print():
    print()
    for row in range(size):
        for col in range(size):
            print(new_maze[row][col], end=' ')
        print()
    print()

# Safe or Not
def isSafe(maze, row, col, size):
    return(row >= 0 and row < size and col >= 0 and col < size and maze[row][col] == 1)

# Place properly
def place_proper(maze, row, col, size, new_maze):
    if row == size - 1 and col == size - 1:
        new_maze[row][col] = 1
        return True
    if isSafe(maze, row, col, size):
        new_maze[row][col] = 1
        if place_proper(maze, row + 1, col, size, new_maze): 
            return True 
        if place_proper(maze, row, col + 1, size, new_maze):
            return True
        else:
            new_maze[row][col] = 0
    return False

# Main
def main():
    print(' Given Maze')
    maze_print()
    place_proper(maze, 0, 0, size, new_maze)
    print(' Solved Maze')
    new_maze_print()

# Driver
if __name__ == '__main__':
    print('\n\t\t ---- RAT IN MAZE ----\n\n')
    main()
    