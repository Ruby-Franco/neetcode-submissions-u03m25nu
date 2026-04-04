class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [ [0, 1], [1, 0], [-1, 0] ,[0, -1]]
        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(row, col):
            q = deque()
            q.append((row,col))
            grid[row][ col] = "0"

            while q: 
                currR, currC = q.popleft()
                
                for rd, cd in directions: 
                    neighborR, neighborC = rd + currR, cd + currC
                    if neighborR < 0 or neighborC < 0 or neighborR >= ROWS or neighborC >= COLS or grid[neighborR][neighborC] == "0":
                        continue
                    else:
                        q.append((neighborR, neighborC))
                        grid[neighborR][neighborC] = "0"                

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1

        return islands