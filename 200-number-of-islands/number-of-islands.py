class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
            



        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))


        def DFS(grid,visited, row, col):
            if not inbound(row,col) or grid[row][col] =='0' or visited[row][col]:
                return 

            
            visited[row][col] = True
            for change_row , change_col in directions:
                new_row = row + change_row
                new_col = col + change_col
            
                DFS(grid,visited ,new_row , new_col)
        island = 0
        for i in range(len(grid)):
            for j in  range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    island += 1
                    DFS(grid,visited,i,j)

        return island



 

        