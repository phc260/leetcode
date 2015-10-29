class Solution {
public:
    std::vector<int> twoSum(std::vector<int> &numbers, int target) {
        std::unordered_map<int, int> hashmap;
        std::vector<int> ans;
        
        for(int i=0; i<numbers.size(); ++i)
            hashmap[numbers[i]] = i;
            
        for(int i=0; i<numbers.size(); ++i) {
            int val = target - numbers[i];
            
            if(hashmap.find(val)!=hashmap.end() && hashmap[val]!=i) {
				ans.push_back(i+1);
				ans.push_back(hashmap[val]+1);
				break;
            }
        }
        return ans;
    }
};
