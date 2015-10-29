class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        I, J, K, L = max(A, E), max(B, F), min(C, G), min(D, H)
        return (A-C)*(B-D) + (E-G)*(F-H) - ((I-K) *(J-L) if(I<K and J<L) else 0)
