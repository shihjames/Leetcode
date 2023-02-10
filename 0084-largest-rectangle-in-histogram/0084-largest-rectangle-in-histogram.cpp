class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int res = 0;
        stack<pair<int, int>> stk;

        for (int i = 0; i < heights.size(); i++) {
            int start = i;
            while (!stk.empty() && stk.top().second > heights[i]) {
                int index = stk.top().first;
                int height = stk.top().second;
                stk.pop();
                res = max(res, height * (i - index));
                start = index;
            }
            stk.push(make_pair(start, heights[i]));
        }

        while (!stk.empty()) {
            res = max(res, (int) (stk.top().second * (heights.size() - stk.top().first)));
            stk.pop();
        }

        return res;
    }
};