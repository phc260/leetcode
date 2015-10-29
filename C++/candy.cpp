class Solution {
public:
    int candy(std::vector<int> &ratings) {
        int n = ratings.size();
        std::vector<int> candies (n, 1);
        for(int i=1; i<n; ++i)
            if(ratings[i]>ratings[i-1])
                candies[i] = 1+candies[i-1];
        for(int i= n-1; i>0; --i)
            if(ratings[i-1]>ratings[i] && candies[i-1]<=candies[i])
                candies[i-1] = 1+candies[i];
        return std::accumulate(candies.begin(), candies.end(), 0);
    }
};
