class Solution {
private:
    void DFS(std::vector<int> &nums, int start, std::vector<int> &partial, std::vector<std::vector<int>> &ans) {
        for(int i=start; i<nums.size(); ++i) {
            partial.push_back(nums[i]);
            ans.push_back(partial);
            DFS(nums, i+1, partial, ans);
            partial.pop_back();
        }
    }
public:
    std::vector<std::vector<int>> subsets(std::vector<int> &nums) {
        std::vector<std::vector<int>> ans(1, std::vector<int>());
        std::vector<int> partial;
        std::sort(nums.begin(), nums.end());
        DFS(nums, 0, partial, ans);
        return ans;
    }
};

