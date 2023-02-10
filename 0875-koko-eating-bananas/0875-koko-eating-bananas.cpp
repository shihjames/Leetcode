#include <vector>

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1, right = *max_element(piles.begin(), piles.end());
        int mid, result = right;

        while (left <= right) {
            mid = left + (right - left) / 2;
            long time = 0;
            for (int pile: piles) {
                time += ceil((double) pile / mid);
            }
            if (time <= h) {
                result = min(result, mid);
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return result;
    }
};