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
    int max_path_sum = INT_MIN;
    int path_sum(TreeNode* root) {
        if(!root) return 0;
        int left = path_sum(root->left);
        int right = path_sum(root->right);
        int sum = root->val;
        if(left>0) sum += left;
        if(right>0) sum += right;
        max_path_sum = std::max(max_path_sum, sum);
        return std::max(0, std::max(left, right)) + root->val;
    }
public:
    int maxPathSum(TreeNode* root) {
        path_sum(root);
        return max_path_sum;
    }
};

