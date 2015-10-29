class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int I = std::max(A, E);
        int J = std::max(B, F);
        int K = std::min(C, G);
        int L = std::min(D, H);
        return (A-C)*(B-D) + (E-G)*(F-H) - (I<K && J<L ? (I-K)*(J-L) : 0);
    }
};

