/**
 *  * Definition for binary tree
 *   * struct TreeNode {
 *    *     int val;
 *     *     TreeNode *left;
 *      *     TreeNode *right;
 *       *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 *        * };
 *         */
class BSTIterator {
private:
    std::stack<TreeNode*> stk;
    void go_left(TreeNode* node) {
        while(node) {
            stk.push(node);
            node = node->left;
        }
    }
public:
    BSTIterator(TreeNode *root) {
        go_left(root);
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !stk.empty();
    }

    /** @return the next smallest number */
    int next() {
        
        auto top = stk.top();
        stk.pop();
        go_left(top->right);
        return top->val;
    }
};

/**
 *  * Your BSTIterator will be called like this:
 *   * BSTIterator i = BSTIterator(root);
 *    * while (i.hasNext()) cout << i.next();
 *     */

