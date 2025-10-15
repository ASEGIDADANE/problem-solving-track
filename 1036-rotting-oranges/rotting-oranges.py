class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        queue = deque()

        time , fresh = 0, 0

        directions = [[0,1], [1,0], [0,-1], [-1,0]] 

        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) 

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append([i,j])
        
        while queue and fresh > 0:

            for _ in range(len(queue)):
                rdi, cdi = queue.popleft()
                for r,c in directions:
                    new_c = cdi + c
                    new_r = rdi + r 
                    if inbound(new_r,new_c):
                        if grid[new_r][new_c]==1:
                        
                            grid[new_r][new_c] = 2
                            queue.append([new_r,new_c])
                            fresh -= 1
            time += 1
        if fresh == 0:
            return time
        else:
            return -1
                    


            
        