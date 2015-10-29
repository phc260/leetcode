class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        
        n = len(ratings)
        
        candy = [1]*n
        
        for i in xrange(1, n):
            if ratings[i]>ratings[i-1]:
                candy[i] = candy[i-1]+1

        for i in xrange(n-1, 0, -1):
            if ratings[i-1]>ratings[i] and candy[i-1]<=candy[i]:
                candy[i-1] = candy[i]+1

        return sum(candy)

