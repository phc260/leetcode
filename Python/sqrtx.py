class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        def binary_search(start, end, target):
            if start<end:
                mid = (start+end)/2
                sq = mid*mid
                if sq==target:
                    return mid
                elif target<sq:
                    return binary_search(start, mid, target)
                else:
                    return binary_search(mid+1, end, target)
            return end-1
                
        return binary_search(1, x+1, x)
