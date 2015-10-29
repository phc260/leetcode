class Solution:
    # @return an integer
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        ans =  0
        
        while i<j:
            area = min(height[i], height[j]) * abs(i-j)
            ans = max(ans, area)
            if height[i]<height[j]: i+=1
            else: j-=1
            
        return ans