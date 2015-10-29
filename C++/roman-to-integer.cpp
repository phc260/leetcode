class Solution {
public:
    int romanToInt(std::string s) {
        std::unordered_map<char, int> dic({{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}});
        int ans = 0;
        int prev_c2n = 10000;
        int curr_c2n = 0;
        for(char c : s) {
            curr_c2n = dic[c];
            ans += curr_c2n;
            if(prev_c2n<curr_c2n) {
                ans -= prev_c2n<<1;
            }
            prev_c2n = curr_c2n;
        }
        return ans;
    }
};

