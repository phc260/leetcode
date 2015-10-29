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
    std::vector<int> inorderTraversal(TreeNode* root) {
        std::stack<TreeNode*> stk;
        std::vector<int> ans;
        while(root || !stk.empty()) {
            while(root) {
                stk.push(root);
                root = root->left;
            }
            root = stk.top();
            stk.pop();
            ans.push_back(root->val);
            root = root->right;
        }
        return ans;
    }
};

