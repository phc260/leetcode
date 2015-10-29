class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if not grid: return 0
        r = len(grid)
        c = len(grid[0])
        stk = []
        islands = 0
        for i in xrange(r):
            for j in xrange(c):
                if grid[i][j]=='1':
                    stk.append((i, j))
                    while stk:
                        x, y = stk.pop()
                        grid[x][y] = '@'
                        if x>0 and grid[x-1][y]=='1': stk.append((x-1, y))
                        if x+1<r and grid[x+1][y]=='1': stk.append((x+1, y))
                        if y>0 and grid[x][y-1]=='1': stk.append((x, y-1))
                        if y+1<c and grid[x][y+1]=='1': stk.append((x, y+1))
                    islands += 1
        return islands
