class Solution {
private:
    void reverse(std::vector<int>& nums, int start, int end) {
        --end;
        while(start<end) {
            std::swap(nums[start], nums[end]);
            ++start;
            --end;
        }
    }
public:
    void rotate(std::vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;
        reverse(nums, 0, n);
        reverse(nums, 0, k);
        reverse(nums, k, n);
    }
};

