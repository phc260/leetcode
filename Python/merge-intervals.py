# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        
        intervals.sort(key = lambda x:x.start)
        
        ans = []
        
        for i in intervals:
            if ans:
                n = len(ans)
                if ans[n-1].start<=i.start<=ans[n-1].end:
                    ans[n-1].end = max(ans[n-1].end, i.end)
                else:
                    ans.append(i)
            else:
                ans.append(i)
            
        return ans