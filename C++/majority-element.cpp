class Solution {
public:
    int majorityElement(std::vector<int> &num) {
        int candidate = 0;
        int count = 0;
        for(int i=0; i<num.size(); ++i) {
            if(count==0) {
                candidate = num[i];
                count = 1;
            } else if(num[i]==candidate) {
                ++count;
            } else {
                --count;
            }
        }
        return candidate;
    }
};
