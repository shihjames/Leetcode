class Solution {
public:
    string minWindow(string s, string t) {
        size_t m = s.size(), n = t.size();
        if (m < n) {
            return "";
        }

        unordered_map<char, int> counter;
        int resStart = 0, resLen = INT_MAX;

        for (char c: t) {
            counter[c]++;
        }

        int left = 0, need = n;
        for (int right = 0; right < m; right++) {
            if (counter.find(s[right]) != counter.end()) {
                counter[s[right]]--;
                if (counter[s[right]] >= 0) {
                    need--;
                }
            }
            while (left <= right && need == 0) {
                if (right - left + 1 < resLen) {
                    resLen = right - left + 1;
                    resStart = left;
                }
                if (counter.find(s[left]) != counter.end()) {
                    counter[s[left]]++;
                    if (counter[s[left]] > 0) {
                        need++;
                    }
                }
                left++;
            }
        }
        if (resLen != INT_MAX) {
            return s.substr(resStart, resLen);
        } else {
            return "";
        }
    }
};