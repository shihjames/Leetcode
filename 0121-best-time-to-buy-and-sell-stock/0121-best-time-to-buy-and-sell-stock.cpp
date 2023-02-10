class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = prices[0], maxRev = 0;
        for (int i = 1; i < prices.size(); i++) {
            minPrice = min(minPrice, prices[i]);
            maxRev = max(maxRev, prices[i] - minPrice);
        }

        return maxRev;
    }
};