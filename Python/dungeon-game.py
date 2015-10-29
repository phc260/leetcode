class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        
        m = len(dungeon)
        n = len(dungeon[0])
        
        hp = [[0]*n for i in xrange(m)]
        hp[m-1][n-1] = max(1-dungeon[m-1][n-1], 1)
        
        for i in xrange(m-2,-1,-1):
            hp[i][n-1] = max(hp[i+1][n-1]-dungeon[i][n-1], 1)
        for j in xrange(n-2,-1,-1):
            hp[m-1][j] = max(hp[m-1][j+1]-dungeon[m-1][j], 1)
        
        for i in xrange(m-2,-1,-1):
            for j in xrange(n-2,-1,-1):
                down = max(hp[i+1][j]-dungeon[i][j], 1)
                right = max(hp[i][j+1]-dungeon[i][j], 1)
                
                hp[i][j] = min(down, right)

        return hp[0][0]
