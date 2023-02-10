class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> wordMap;
        for (auto str: strs) {
            string key = genKey(str);
            wordMap[key].push_back(str);
        }

        vector<vector<string>> res;
        for (auto it = wordMap.begin(); it != wordMap.end(); it++) {
            res.push_back(it->second);
        }

        return res;
    }

private:
    string genKey(string s) {
        vector<int> counter(26, 0);
        for (auto chr: s) {
            counter[int(chr) - int('a')]++;
        }

        string key;
        for (auto count: counter) {
            key.append(to_string(count) + "#");
        }

        return key;
    }
};