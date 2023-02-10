#include <stack>

class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> parenMap = {{')', '('}, {']', '['}, {'}', '{'}};
        stack<char> st;

        for (char c: s) {
            if (c == '(' || c == '[' || c == '{') {
                st.push(c);
            } else {
                if (st.empty() || parenMap[c] != st.top()) {
                    return false;
                } else {
                    st.pop();
                }
            }
        }

        return st.size() == 0;
    }
};