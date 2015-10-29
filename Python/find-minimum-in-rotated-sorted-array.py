class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        n = len(num)
        for i in range(1, n):
            if num[i] < num[0]:
                return num[i]
                
        return num[0]
