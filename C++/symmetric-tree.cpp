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
private:
    bool isSymmetric(TreeNode* n1, TreeNode* n2) {
    if(!n1) return !n2;
    if(!n2) return false;
    if(n1->val!=n2->val) return false;
    if(!isSymmetric(n1->left, n2->right)) return false;
    if(!isSymmetric(n1->right, n2->left)) return false;
    return true;
}
public:
    bool isSymmetric(TreeNode* root) {
        return isSymmetric(root, root);
    }
};

