#include <stack>

class MinStack {
public:
    MinStack() {
    }
    
    void push(int val) {
        pair<int, int> valPair;
        if (mStk.empty()) {
            valPair = make_pair(val, val);
        } else {
            valPair = make_pair(val, min(val, mStk.top().second));
        }
        mStk.push(valPair);
    }
    
    void pop() {
        mStk.pop();
    }
    
    int top() {
        return mStk.top().first;
    }
    
    int getMin() {
        return mStk.top().second;
    }

private:
    stack<pair<int, int>> mStk;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */