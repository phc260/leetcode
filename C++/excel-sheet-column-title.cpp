class Solution {
public:
    std::string convertToTitle(int n) {
        std::string title;
        do {
            title += ((n-1)%26)+'A';
            n = (n-1)/26;
        } while(n);
        std::reverse(title.begin(), title.end());
        return title;
    }
};

