class Solution {
public:
    void solve(std::vector<std::vector<char>>& board) {
        if(board.size()<3 || board[0].size()<3) return;
        int r = board.size();
        int c = board[0].size();
        std::stack<std::pair<int,int>> stk;
        for(int i=0; i<r; ++i) {
            if(board[i][0]=='O') stk.push(std::pair<int,int>(i, 0));
            if(board[i][c-1]=='O') stk.push(std::pair<int,int>(i, c-1));
        }
        
        for(int j=0; j<c; ++j) {
            if(board[0][j]=='O') stk.push(std::pair<int,int>(0, j));
            if(board[r-1][j]=='O') stk.push(std::pair<int,int>(r-1, j));
        }
        
        while(!stk.empty()) {
            int x = stk.top().first
            int y = stk.top().second;
            stk.pop();
            board[x][y] = '@';
            if(x>0 && board[x-1][y]=='O') stk.push(std::pair<int,int>(x-1, y));
            if(x+1<r && board[x+1][y]=='O') stk.push(std::pair<int,int>(x+1, y));
            if(y>0 && board[x][y-1]=='O') stk.push(std::pair<int,int>(x, y-1));
            if(y+1<r && board[x][y+1]=='O') stk.push(std::pair<int,int>(x, y+1));
            
        }
        
        for(int i=0; i<r; ++i) {
            for(int j=0; j<c; ++j) {
                if(board[i][j]=='O') board[i][j] = 'X';
                if(board[i][j]=='@') board[i][j] = 'O';
            }
        }
    }
};

