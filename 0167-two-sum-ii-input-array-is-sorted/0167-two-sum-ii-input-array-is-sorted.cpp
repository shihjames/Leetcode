class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size() - 1;
        int curSum = 0;
        vector<int> res = {-1, -1};

        while (left < right) {
            curSum = numbers[left] + numbers[right];
            if (curSum > target) {
                right--;
            } else if (curSum < target) {
                left++;
            } else {
                res[0] = left + 1;
                res[1] = right + 1;
                return res;
            }
        }

        return res;
    }
};