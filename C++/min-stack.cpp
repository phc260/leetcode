class MinStack {
private:
    std::stack<int> stk;
    std::stack<int> min_val_stk;
public:
    void push(int x) {
        stk.push(x);
        if(!min_val_stk.empty())
            min_val_stk.push(std::min(min_val_stk.top(), x));
        else
            min_val_stk.push(x);
    }

    void pop() {
        stk.pop();
        min_val_stk.pop();
    }

    int top() {
        return stk.top();
    }

    int getMin() {
        return min_val_stk.top();
    }
};

