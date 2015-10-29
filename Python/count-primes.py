class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n<3: return 0
        pool = [True]*2 + [True, False]*((n-2)/2) + ([True] if n%2==1 else [])
        count_prime = 1

        i = 3
        while i<n:
            while i<n and pool[i]:
                i += 1
            if i>=n: break
            num = i
            count_prime += 1
            for j in xrange(num, n, num):
                pool[j] = True

        return count_prime

