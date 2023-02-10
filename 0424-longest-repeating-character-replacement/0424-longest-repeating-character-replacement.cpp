#include <vector>

class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0, res = 0;
        // current highest frequency
        int curFreq;
        vector<int> counter(26, 0);
        for (int right; right < s.size(); right++) {
            // update counter while right pointer keep going right
            counter[s[right] - 'A']++;
            // find the highest frequency
            curFreq = *max_element(counter.begin(), counter.end());
            // move left pointer if it is not a valid substring for replacement
            while ((right - left + 1) - curFreq > k) {
                    counter[s[left] - 'A']--;
                    left++;
                    // update current highest frequency
                    curFreq = *max_element(counter.begin(), counter.end());
            }
            // update res
            res = max(res, right - left + 1);
        }
        return res;
    }
};