class Solution {
private:
    static bool cmp(int a, int b) {
        std::string m=to_string(a), n=to_string(b);
        return m+n>n+m;
    }
public:
    string largestNumber(std::vector<int>& nums) {
        std::string ans;
        std::sort(nums.begin(), nums.end(), cmp);
        for(int n : nums) ans+=std::to_string(n);
        return ans.front()!='0' ? ans : "0";
    }
};

