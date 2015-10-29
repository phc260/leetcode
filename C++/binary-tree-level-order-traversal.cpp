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
    void traverse(TreeNode *root, int level, std::vector<std::vector<int>> &ans) {
        if(root) {
            if(level>=ans.size()) ans.push_back(std::vector<int>());
            ans[level].push_back(root->val);
            traverse(root->left, level+1, ans);
            traverse(root->right, level+1, ans);
        }
    }
public:
    vector<vector<int>> levelOrder(TreeNode *root) {
        std::vector<std::vector<int>> ans;
        traverse(root, 0, ans);
        return ans;
    }
};

