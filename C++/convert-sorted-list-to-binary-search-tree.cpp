/**
 *  * Definition for singly-linked list.
 *   * struct ListNode {
 *    *     int val;
 *     *     ListNode *next;
 *      *     ListNode(int x) : val(x), next(NULL) {}
 *       * };
 *        */
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
    TreeNode* BST(std::vector<int> &nums, int start, int end) {
        TreeNode* node = NULL;
        if(start<end) {
            int mid = (start+end)/2;
            node = new TreeNode(nums[mid]);
            node->left = BST(nums, start, mid);
            node->right = BST(nums, mid+1, end);
        }
        return node;
    }
    TreeNode* sortedArrayToBST(std::vector<int> &nums) {
        return BST(nums, 0, nums.size());
    }
public:
    TreeNode* sortedListToBST(ListNode* head) {
        std::vector<int> nums;
        while(head) {
            nums.push_back(head->val);
            head = head->next;
        }
        return sortedArrayToBST(nums);
    }
};

