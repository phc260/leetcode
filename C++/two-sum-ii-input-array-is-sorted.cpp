class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& numbers, int target) {
        std::vector<int> ans {0, 0};
        std::unordered_hahmap<int,int> hahmap;
        int val;
        for(int i=0; i<numbers.size(); ++i) hahmap[numbers[i]] = i;
        for(int i=0; i<numbers.size(); ++i) {
            val = target-numbers[i];
            if(hahmap.find(val)!=hahmap.end() && i!=hahmap[val]) {
                ans[0] = i+1;
                ans[1] = hahmap[val]+1;
                break;
            }
        }
        return ans;
    }
};

