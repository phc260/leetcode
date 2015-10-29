class Solution {
public:
    int maxSubArray(std::vector<int> &nums) {
        int sum = 0;
        int maxsum = nums[0];
        
        for(auto i : nums) {
            sum += i;
            if(sum>maxsum) maxsum = sum;
            if(sum<0) sum = 0;
        }
        return maxsum;
    }
};
