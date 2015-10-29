class Solution {
private:
    bool is_valid(std::vector<std::vector<char>> &board, int i, int j) {
        int val = board[i][j];
        board[i][j] = '.';
        for(int k=0; k<9; ++k) {
            if(board[i][k]==val || board[k][j]==val || board[(i/3)*3+k/3][(j/3)*3+k%3]==val) {
                board[i][j] = val;
                return false;
            }
        }
        board[i][j] = val;
        return true;
    }
    bool DFS(std::vector<std::vector<char>> &board) {
        std::string numbers = "123456789";
        for(int i=0; i<9; ++i) {
            for(int j=0; j<9; ++j) {
                if(board[i][j]=='.') {
                    for(char k : numbers) {
                        board[i][j] = k;
                        if(is_valid(board, i, j) && DFS(board))
                            return true;
                    }
                    board[i][j] = '.';
                    return false;
                }
            }
        }
        return true;
    }
public:
    void solveSudoku(vector<vector<char>> &board) {
        DFS(board);
    }
};
