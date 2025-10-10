class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        visited = set()

        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
       
        def inBound(row , col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
                
    
        def DFS(row,col):
            permimeter = 0

            if not inBound(row , col) or grid[row][col] == 0:
                return 1

            if (row,col) in  visited:
                return 0
            visited.add((row, col))
            
            for change_row , change_col in  direction:

                new_row = row + change_row
                new_col = col + change_col
                permimeter +=  DFS(new_row , new_col)

            return permimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return DFS(i,j)
        
             

            

        
        