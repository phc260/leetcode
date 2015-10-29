// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        int total = 0;
        bool eof = false;
        int bytes = 0;
        while(!eof && total<n) {
            bytes = read4(buf+total);
            if(bytes<4) eof = true;
            bytes = std::min(bytes, n-total);
            total += bytes;
        }
        return total;
    }
};