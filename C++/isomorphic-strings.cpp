class Solution {
public:
    bool isIsomorphic(std::string s, std::string t) {
        std::unordered_map<char, char> hashmap_s;
        std::unordered_map<char, char> hashmap_t;
        
        for(int i=0; i<s.size(); ++i) {
            if(hashmap_s.find(s[i])!=hashmap_s.end()) {
                if(hashmap_s[s[i]]!=t[i]) return false;
            }
            else {
                hashmap_s[s[i]] = t[i];
            }
            if(hashmap_t.find(t[i])!=hashmap_t.end()) {
                if(hashmap_t[t[i]]!=s[i]) return false;
            }
            else {
                hashmap_t[t[i]] = s[i];
            }
        }
        return true;
    }
};

