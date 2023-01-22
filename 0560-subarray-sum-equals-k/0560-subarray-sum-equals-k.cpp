class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        /* use hashmap to count the # of same value of sums in different subarray */
        unordered_map<int, int> counter;
        int res = 0, accSum = 0;
        counter[0] = 1;
        
        for (int num: nums) {
            accSum += num;
            if (counter.find(accSum - k) != counter.end()) {
                /* found current sequence can sum equals k by removing prefix */
                res += counter[accSum - k];
            }
            counter[accSum]++;
        }
        
        return res;
    }
};