class Solution {
public:
    std::vector<std::vector<int>> generateMatrix(int n) {
        std::vector<std::vector<int>> mat (n, std::vector<int>(n, 0));
        int start = 0, end = n-1, x = 1;
        while(start<end) {
            for(int i=0; i<end-start; ++i) mat[start][start+i] = x++;
            for(int i=0; i<end-start; ++i) mat[start+i][end] = x++;
            for(int i=0; i<end-start; ++i) mat[end][end-i] = x++;
            for(int i=0; i<end-start; ++i) mat[end-i][start] = x++;
            ++start;
            --end;
        }
        if(start==end) mat[start][start] = x;
        return mat;
    }
};

