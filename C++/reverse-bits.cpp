class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ans;
        for(uint32_t i=0; i<32; ++i) {
            ans <<= 1;
            ans |= n&1;
            n >>= 1;
        }
        return ans;
    }
};

