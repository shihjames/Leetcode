class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int last_index = n - 1;
        for (int i = n - 2; i >= 0; i--) {
            if (nums.at(i) + i >= last_index) {
                last_index = i;
            }
        }
        return last_index == 0;
    }
};