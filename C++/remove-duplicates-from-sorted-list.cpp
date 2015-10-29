/**
 *  * Definition for singly-linked list.
 *   * struct ListNode {
 *    *     int val;
 *     *     ListNode *next;
 *      *     ListNode(int x) : val(x), next(NULL) {}
 *       * };
 *        */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *p1, *p2, *del;
        p1 = head;
        while(p1) {
            p2 = p1->next;
            while(p2 && p1->val==p2->val) {
                del = p2;
                p2 = p2->next;
                delete del;
            }
            p1->next = p2;
            p1 = p1->next;
        }
        return head;
    }
};

