class Solution {
private:
    int binary_search(std::vector<int> &nums, int start, int end, int target) {
        if(start<end) {
            int mid = (start+end)/2;
            if(nums[mid]==target) return mid;
            else if(target<nums[mid]) return binary_search(nums, start, mid, target);
            else return binary_search(nums, mid+1, end, target);
        }
        return -1;
    }
public:
    std::vector<int> searchRange(std::vector<int> &nums, int target) {
        
        int idx = binary_search(nums, 0, nums.size(), target);
        if(idx==-1)
            return std::vector<int> {-1, -1};
        else {
            int i=idx-1, j=idx+1;
            while(i>=0 && nums[i]==nums[idx]) --i;
            while(j<nums.size() && nums[j]==nums[idx]) ++j;
            return std::vector<int> {i+1, j-1};
        }
    }
};

