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
    ListNode* swapPairs(ListNode* head) {
        ListNode *prev, *fake, *p1, *p2;
        prev = fake = new ListNode(0);
        fake->next = head;
        while(prev->next && prev->next->next) {
            p1 = prev->next;
            p2 = p1->next;
            prev->next = p2;
            p1->next = p2->next;
            p2->next = p1;
            prev = p1;
        }
        head = fake->next;
        delete fake;
        return head;
    }
};

