#include <stack>

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;

        for (string token: tokens) {
            if (token.size() > 1 || isdigit(token[0])) {
                st.push(stoi(token));
            } else {
                int op2 = st.top();
                st.pop();
                int op1 = st.top();
                st.pop();

                switch (token[0]) {
                    case '+':
                        st.push(op1 + op2);
                        break;
                    case '-':
                        st.push(op1 - op2);
                        break;
                    case '*':
                        st.push(op1 * op2);
                        break;
                    case '/':
                        st.push((int) (op1 / op2));
                        break;
                }
            }
        }

        return st.top();
    }
};