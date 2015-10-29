class Solution {
public:
    int maxProduct(std::vector<int>& nums) {
        int global_max = nums[0];
        int local_min = nums[0];
        int local_max = nums[0];
        int t_max, t_min;
        for(int i=1; i<nums.size(); ++i) {
            t_max = local_max;
            t_min = local_min;
            local_max = std::max(nums[i], std::max(t_max*nums[i], t_min*nums[i]));
            local_min = std::min(nums[i], std::min(t_max*nums[i], t_min*nums[i]));
            global_max = std::max(global_max, local_max);
        }
        return global_max;
    }
};

