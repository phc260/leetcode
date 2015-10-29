class Solution {
public:
    // Newton's Method
    int mySqrt(int x) {
        double x0=1.0;
        do{
            x0 = (x0+ x/x0)/2;
        }while(abs(pow(x0, 2) - x) >= 1);
        return (int)x0;
    }
};
