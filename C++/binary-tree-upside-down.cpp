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
    TreeNode* upsideDownBinaryTree(TreeNode* root, TreeNode* parent=NULL) {
        if(!root) return parent;
        TreeNode* new_root = upsideDownBinaryTree(root->left, root);
        root->left = parent ? parent->right : NULL;
        root->right = parent;
        return new_root;
    }
};

