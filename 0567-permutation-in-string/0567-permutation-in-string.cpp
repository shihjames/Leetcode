class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        size_t m = s1.size(), n = s2.size();
        if (m > n) {
            return false;
        }
        // create counter for current window
        vector<int> counter(26, 0);
        for (int i = 0; i < m; i++) {
            counter[s1[i] - 'a']++;
            counter[s2[i] - 'a']--;
        }

        // count zeros, if all zeros means matched
        if (isMatched(counter)) {
            return true;
        }
        
        // slide the window to the right and check each time
        for (int i = m; i < n; i++) {
            counter[s2[i] - 'a']--;
            counter[s2[i - m] - 'a']++;
            if (isMatched(counter)) {
                return true;
            }
        }

        return false;
    }

private:
    bool isMatched(vector<int> &counter) {
        for (auto c: counter) {
            if (c != 0) {
                return false;
            }
        }

        return true;
    }
};