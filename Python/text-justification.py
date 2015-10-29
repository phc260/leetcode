class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        text = ' '.join(words)+' '
        ans = []
        while text:
            idx = text.rfind(' ', 0, maxWidth+1)
            line = text[:idx].split()
            l, n = sum(len(w) for w in line), len(line)
            if n==1:
                ans.append(line[0].ljust(maxWidth))
            else:
                s, remainder = divmod(maxWidth-l, n-1)
                line[:-1] = [w+' '*s for w in line[:-1]]
                line[:remainder] = [w+' ' for w in line[:remainder]]
                ans.append(''.join(line))
            text = text[idx+1:]
        ans[-1] = ' '.join(ans[-1].split()).ljust(maxWidth)
        return ans
