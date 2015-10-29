class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k==0 or t<0: return False
        dic = collections.OrderedDict()
        for i in nums:
            key = i if t==0 else i//t
            for j in (dic.get(key-1), dic.get(key), dic.get(key+1)):
                if j is not None and abs(i-j)<=t: return True
            if len(dic)==k: dic.popitem(False)
            dic[key] = i
        return False
