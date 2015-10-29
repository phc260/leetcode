class Solution {
public:
    std::vector<std::string> summaryRanges(std::vector<int> &nums) {
        std::vector<std::string> ans;
        int n = nums.size();
        int start, end;
        for(int i=0; i<n;) {
            start = end = i;
            while(end+1<n && nums[end]+1==nums[end+1]) ++end;
            if(start<end) ans.push_back(std::to_string(nums[start])+"->"+std::to_string(nums[end]));
            else ans.push_back(std::to_string(nums[start]));
            i = end+1;
        }
        return ans;
    }
};

