class Solution {
public:
    vector<string> generateParenthesis(int n) {
        int left_count = 0, right_count = 0;
        vector<string> res;
        helper(res, "", n, left_count, right_count);
        return res;
    }

private:
    void helper(vector<string> &res, string cur, int n, int left, int right) {
        if (left == n && right == n) {
            res.push_back(cur);
            return;
        }

        if (left < n) {
            helper(res, cur + "(", n, left + 1, right);
        }

        if (right < left) {
            helper(res, cur + ")", n, left, right + 1);
        }
    }
};