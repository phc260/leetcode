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
    int kthSmallest(TreeNode* root, int k) {
        std::stack<TreeNode*> stk;
        while(root || !stk.empty()) {
            while(root) {
                stk.push(root);
                root = root->left;
            }
            root = stk.top();
            stk.pop();
            --k;
            if(k==0) return root->val;
            root = root->right;
        }
        return 0;
    }
};

