class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        C = []
        
        i = j = 0
        m = len(nums1)
        n = len(nums2)
        
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                C.append(nums1[i])
                i += 1
            else:
                C.append(nums2[j])
                j += 1
                
        while i<m:
            C.append(nums1[i])
            i += 1
            
        while j<n:
            C.append(nums2[j])
            j += 1
            
        o = len(C)
        if o%2==1:
            return float(C[o/2])
        else:
            return float(C[o/2]+C[o/2-1])/2