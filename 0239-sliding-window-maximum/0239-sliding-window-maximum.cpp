#include <deque>

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> res;

        int left = 0;
        for (int right = 0; right < nums.size(); right++) {
            // maintain a descending order
            while (!dq.empty() && nums[dq.back()] < nums[right]) {
                dq.pop_back();
            }

            dq.push_back(right);

            // left edge start to slide to maintain same window length
            if (right >= k - 1) {
                res.push_back(nums[dq.front()]);
                left++;
                // pop out element outside the window
                if (left > dq.front()) {
                    dq.pop_front();
                }
            }
        }

        return res;
    }
};