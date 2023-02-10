class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size(), 0);
        stack<pair<int, int>> stk;

        int index;
        for (int i = 0; i < temperatures.size(); i++) {
            while (!stk.empty() && stk.top().first < temperatures[i]) {
                index = stk.top().second;
                res[index] = (i - index);
                stk.pop();
            }
            stk.push(make_pair(temperatures[i], i));
        }

        return res;
    }
};