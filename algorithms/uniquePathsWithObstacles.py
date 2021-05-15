## Given a grid of size m * n, let us assume you are starting at (1, 1) and your goal is to reach (m, n). At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y). Now consider if some obstacles are added to the grids. How many unique paths would there be? An obstacle and empty space are marked as 1 and 0 respectively in the grid.

def uniquePathsWithObstacles(A):
    # create a 2D-matrix and initializing with value 0
    print("Length of A ",len(A))
    paths = [[0] * len(A[0]) for i in A]

    # initializing the left corner if no obstacle there
    if A[0][0] == 0:
        paths[0][0] = 1

    # initializing first column of the 2D matrix
    for i in range(1, len(A)):
        if A[i][0] == 0:
            paths[i][0] = paths[i - 1][0]
    print("First for loop ",paths)
        # initializing first row of the 2D matrix


    for j in range(1, len(A[0])):
        if A[0][j] == 0:
            paths[0][j] = paths[0][j - 1]

    print("Second for loop ", paths)

    for i in range(1, len(A)):
        for j in range(1, len(A[0])):

            # If current cell is not obstacle
            if A[i][j] == 0:
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]


    print("Last value",paths)
    return paths[-1][-1]    

# Driver Code
A = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
print(uniquePathsWithObstacles(A))
