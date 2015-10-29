class Solution {
private:
    void reverse_word(std::string &s, int start, int end) {
        end -= 1;
        for(; start<end; ++start, --end) {
            std::swap(s[start], s[end]);
        }
    }
public:
    void reverseWords(std::string &s) {
        int start = 0;
        int end = 0;
        for(; end<s.size(); ++end) {
            if(s[end]==' ') {
                reverse_word(s, start, end);
                start = end+1;
            }
        }
        reverse_word(s, start, end);
        reverse_word(s, 0, s.size());
    }
};
