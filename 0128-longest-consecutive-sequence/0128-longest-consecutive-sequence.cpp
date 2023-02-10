class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int longestLength = 0, curLength = 0, curNum;
        unordered_set<int> numSet;

        for (int num: nums) {
            numSet.insert(num);
        }

        for (int i = 0; i < nums.size(); i++) {
            if (numSet.find(nums[i] - 1) != numSet.end()) {
                continue;
            }

            curLength = 1;
            curNum = nums[i];

            while (numSet.find(curNum + 1) != numSet.end()) {
                curLength++;
                curNum++;
            }

            longestLength = max(longestLength, curLength); 
        }

        return longestLength;
    }
};