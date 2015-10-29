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
public:
    bool isValidSudoku(std::vector<std::vector<char>> &board) {
        for(int i=0; i<9; ++i) {
            for(int j=0; j<9; ++j) {
                if('1'<=board[i][j] && board[i][j]<='9' && !is_valid(board, i, j))
                    return false;
            }
        }
        return true;
    }
};
