class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        counter = [0, 0, 0, 0]
        
        for i in A:
            counter[2] |= counter[1] & i
            counter[1] ^= i
            counter[3] = ~(counter[1] & counter[2])
            counter[1] &= counter[3]
            counter[2] &= counter[3]
        
        return counter[1]