class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> accProduct(nums.size(), 1);

        for (int i = 1; i < accProduct.size(); i++) {
            accProduct[i] = accProduct[i - 1] * nums[i - 1];
        }

        int curProduct = 1;
        for (int i = accProduct.size() - 1; i >= 0; i--) {
            accProduct[i] *= curProduct;
            curProduct *= nums[i];
        }

        return accProduct;
    }
};