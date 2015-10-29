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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *fake = new ListNode(0);
        ListNode *prev = fake, *curr = head;
        fake->next = head;
        
        while(curr) {
            if(curr->val==val) {
                prev->next = curr->next;
                delete curr;
                curr = prev->next;
            }
            else {
                curr = curr->next;
                prev = prev->next;
            }
        }
        head = fake;
        head = head->next;
        delete fake;
        return head;
    }
};

