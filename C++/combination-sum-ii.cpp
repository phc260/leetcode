class Solution {
private:
    void DFS(std::vector<int> &candidates, int start, int target, std::vector<int> &partial, std::vector<std::vector<int>> &ans) {
        if(target==0) {
            ans.push_back(partial);
            return;
        }
        for(int i=start; i<candidates.size() && target>=candidates[i]; ++i) {
            if(i==start || candidates[i-1]!=candidates[i]) {
                partial.push_back(candidates[i]);
                DFS(candidates, i+1, target-candidates[i], partial, ans);
                partial.pop_back();
            }
        }
    }
public:
    std::vector<std::vector<int>> combinationSum2(std::vector<int> &candidates, int target) {
        std::sort(candidates.begin(), candidates.end());
        std::vector<int> partial;
        std::vector<std::vector<int>> ans;
        DFS(candidates, 0, target, partial, ans);
        return ans;
    }
};
