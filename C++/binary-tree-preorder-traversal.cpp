/**
 *  * Definition for a binary tree node.
 *   * struct TreeNode {
 *    *     int val;
 *     *     TreeNode *left;
 *      *     TreeNode *right;
 *       *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 *        * };
 *         */
class Solution {
public:
    std::vector<int> preorderTraversal(TreeNode* root) {
        std::stack<TreeNode*> stk;
        std::vector<int> ans;
        if(root) stk.push(root);
        while(!stk.empty()) {
            root = stk.top();
            ans.push_back(root->val);
            stk.pop();
            if(root->right) stk.push(root->right);
            if(root->left) stk.push(root->left);
        }
        return ans;
    }
};

