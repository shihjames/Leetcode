class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> left(height.size(), 0), right(height.size(), 0);
        int res = 0;

        int curHighest = 0;
        for (int i = 0; i < height.size(); i++) {
            curHighest = max(curHighest, height[i]);
            left[i] = curHighest;
        }

        curHighest = 0;
        for (int i = height.size() - 1; i >= 0; i--) {
            curHighest = max(curHighest, height[i]);
            right[i] = curHighest;
        }

        for (int i = 0; i < height.size(); i++) {
            res += min(left[i], right[i]) - height[i];
        }

        return res;
    }
};