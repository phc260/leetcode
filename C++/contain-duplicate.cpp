class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        return std::set<int>(nums.begin(), nums.end()).size() < nums.size();
    }
};
