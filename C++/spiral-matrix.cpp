class Solution {
public:
    std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
        std::vector<int> ans;
        if(matrix.size()==0) return ans;
        int r = matrix.size();
        int c = matrix[0].size();
        int left=0, right=c-1, top=0, down=r-1;
        while(left<right && top<down) {
            for(int i=0; i<right-left; ++i) ans.push_back(matrix[top][left+i]);
            for(int i=0; i<down-top; ++i) ans.push_back(matrix[top+i][right]);
            for(int i=0; i<right-left; ++i) ans.push_back(matrix[down][right-i]);
            for(int i=0; i<down-top; ++i) ans.push_back(matrix[down-i][left]);
            ++left; --right; ++top; --down;
        }
        if(top==down) {
            for(int i=0; i<right-left+1; ++i) ans.push_back(matrix[top][left+i]);
        }
        else if(left==right) {
            for(int i=0; i<down-top+1; ++i) ans.push_back(matrix[top+i][left]);
        }
        return ans;
    }
};

