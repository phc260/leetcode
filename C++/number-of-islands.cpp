class Solution {
public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        if(grid.empty()) return 0;
        int r = grid.size();
        int c = grid[0].size();
        int islands = 0;
        std::stack<std::pair<int,int>> stk;
        for(int i=0; i<r; ++i) {
            for(int j=0; j<c; ++j) {
                if(grid[i][j]=='1') {
                    stk.push(std::pair<int,int>(i, j));
                    while(!stk.empty()) {
                        int x = stk.top().first;
                        int y = stk.top().second;
                        stk.pop();
                        grid[x][y] = '@';
                        if(x>0 && grid[x-1][y]=='1') stk.push(std::pair<int,int>(x-1, y));
                        if(x+1<r && grid[x+1][y]=='1') stk.push(std::pair<int,int>(x+1, y));
                        if(y>0 && grid[x][y-1]=='1') stk.push(std::pair<int,int>(x, y-1));
                        if(y+1<c && grid[x][y+1]=='1') stk.push(std::pair<int,int>(x, y+1));
                    }
                    ++islands;
                }
            }
        }
        return islands;
    }
};

