class Solution {
public:
    std::vector<int> grayCode(int n) {
        std::vector<int> ans {0};
        int len = 0;
        for(int i=0; i<n; ++i) {
            len = ans.size();
            for(int j=len-1; j>-1; --j) {
                ans.push_back(ans[j]+(1<<i));
            }
        }
        return ans;
    }
};
