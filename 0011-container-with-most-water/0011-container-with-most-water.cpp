class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int left_h, right_h;
        int maxVol = 0;

        int w, h;
        while (left < right) {
            left_h = height[left];
            right_h = height[right];

            w = right - left;
            h = min(left_h, right_h);
            maxVol = max(maxVol, w * h);

            if (left_h < right_h) {
                left++;
            } else {
                right--;
            }
        }

        return maxVol;
    }
};