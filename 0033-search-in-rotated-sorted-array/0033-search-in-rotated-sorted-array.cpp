class Solution {
public:
    int search(vector<int>& nums, int target) {
        int len = nums.size();
        int left = 0, right = len - 1, mid, pivot;

        if (len == 1 || nums[right] > nums[left]) {
            pivot = 0;
        } else {
            while (left <= right) {
                mid = left + (right - left) / 2;
                if (nums[mid] > nums[mid + 1]) {
                    pivot = mid + 1;
                    break;
                } else if (nums[mid] < nums[mid - 1]) {
                    pivot = mid;
                    break;
                } else if (nums[mid] > nums[0]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        if (pivot == 0) {
            return binarySearch(nums, target, pivot, len - 1);
        } else if (nums[pivot] == target) {
            return pivot;
        } else if (target < nums[0]) {
            return binarySearch(nums, target, pivot, len - 1);
        } else {
            return binarySearch(nums, target, 0, pivot);
        }
    }

private:

    int binarySearch(vector<int>& nums, int target, int left, int right) {
        int mid;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return -1;
    }
};