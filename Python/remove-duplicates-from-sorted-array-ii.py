class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):

        if not A:
            return 0
            
        c = 0
        pre = A[0]
        rm = []
                
        for i in A[1:]:
            if i==pre:
                c += 1
                
                if c>1:
                    rm.append(i)
            else:
                c = 0
                
            pre = i
            
        for i in rm:
            A.remove(i)
            
        return len(A)