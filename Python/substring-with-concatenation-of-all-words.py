class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        m = len(words)
        n = len(words[0])
        counter = {}
        ans = []
        for w in words:
            if w in counter: counter[w]+=1
            else: counter[w]=1
        for i in xrange(len(s)+1-m*n):
            found = {}
            for j in xrange(m):
                k = i+j*n
                word = s[k:k+n]
                if word in counter:
                    if word in found:
                        found[word] += 1
                    else:
                        found[word] = 1
                    if found[word]>counter[word]: break
                else: break
            else: ans.append(i)
        return ans
