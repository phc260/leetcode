class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        height.append(0)
        stk = []
        i = area = 0
        while i<len(height):
            if not stk or height[i]>height[stk[-1]]:
                stk.append(i)
            else:
                idx = stk.pop()
                area = max(area, height[idx]*(i-stk[-1]-1 if stk else i))
                i -= 1
            i += 1
        return area
