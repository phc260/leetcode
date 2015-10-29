class Solution {
private:
    void DFS(int k, int n, int start, std::vector<int> &partial, std::vector<std::vector<int>> &ans) {
        if(n<0) return;
        if(k==0 && n==0) {
            ans.push_back(partial);
            return;
        }
        for(int i=start; i<10; ++i) {
            partial.push_back(i);
            DFS(k-1, n-i, i+1, partial, ans);
            partial.pop_back();
        }
    }
public:
    std::vector<std::vector<int>> combinationSum3(int k, int n) {
        std::vector<std::vector<int>> ans;
        std::vector<int> partial;
        DFS(k, n, 1, partial, ans);
        return ans;
    }
};
