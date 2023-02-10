class Solution {
public:
    int findMin(vector<int>& nums) {
        size_t len = nums.size();

        if ((nums[0] < nums[len - 1]) || (len == 1)) {
            return nums[0];
        }

        int left = 0, right = len - 1, mid;

        while (left <= right) {
            mid = left + (right - left) / 2;
            if (nums[mid + 1] < nums[mid]) {
                return nums[mid + 1];
            } else if (nums[mid] < nums[mid - 1]) {
                return nums[mid];
            } else if (nums[mid] > nums[0]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return INT_MAX;
    }
};