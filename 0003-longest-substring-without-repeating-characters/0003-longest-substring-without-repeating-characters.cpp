class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        unordered_map<char, int> charMap;
        
        int left = 0;
        for (int right = 0; right < s.size(); right++) {
            charMap[s[right]]++;
            if (charMap[s[right]] > 1) {
                while (charMap[s[right]] > 1) {
                    charMap[s[left]]--;
                    if (charMap[s[left]] == 0) {
                        charMap.erase(s[left]);
                    }
                    left++;
                }
            }
            res = max(res, right - left + 1);
        }

        return res;
    }
};