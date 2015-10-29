class Solution {
public:
    void sortColors(std::vector<int> &nums) {
        int colors[3] = {0};
        int flag = 0;
        for(int n : nums) colors[n]+=1;
        for(int i=0; i<nums.size(); ++i) {
            while(colors[flag]<=0) ++flag;
            nums[i] = flag;
            --colors[flag];
        }
    }
};

