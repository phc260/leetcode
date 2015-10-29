class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        skyline, alive = [], []
        i, n = 0, len(buildings)
        
        while i<n or alive:
            if not alive or (i<n and buildings[i][0]<=-alive[0][1]):
                x = buildings[i][0]
                while i<n and buildings[i][0]==x:
                    heapq.heappush(alive, [-buildings[i][2], -buildings[i][1]])
                    i += 1
            else:
                x = -alive[0][1]
                while alive and -alive[0][1]<=x:
                    heapq.heappop(alive)
            height = len(alive) and -alive[0][0]
            if not skyline or height!=skyline[-1][1]:
                skyline.append([x, height])
        
        return skyline
