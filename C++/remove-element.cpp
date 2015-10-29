class Solution {
public:
    int removeElement(std::vector<int> &nums, int val) {
        int m = nums.size();
        for(int i=0; i<m; ++i) {
            if(nums[i]==val) {
                int j = m-1;
                for(; nums[j]==val && j>i; --j);
                
                if(j>i) {
                    std::swap(nums[i], nums[j]);
                    --m;
                }
                else
                    m = i;
            }
        }
        return m;
    }
};