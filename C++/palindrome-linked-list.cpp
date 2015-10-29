/**
 *  * Definition for singly-linked list.
 *   * struct ListNode {
 *    *     int val;
 *     *     ListNode *next;
 *      *     ListNode(int x) : val(x), next(NULL) {}
 *       * };
 *        */
class Solution {
private:
    ListNode* reverseList(ListNode* head) {
        ListNode* fake = new ListNode(0);
        ListNode* cur = head;
        ListNode* next;
        while(cur) {
            next = cur->next;
            cur->next = fake->next;
            fake->next = cur;
            cur = next;
        }
        next = fake->next;
        delete fake;
        return next;
    }
public:
    bool isPalindrome(ListNode* head) {
        ListNode *p1, *p2;
        p1 = p2 = head;
        while(p2) {
            p1 = p1->next;
            p2 = p2->next;
            if(p2) p2 = p2->next;
        }
        p1 = reverseList(p1);
        p2 = head;
        while(p1 && p2) {
            if(p1->val!=p2->val) return false;
            p1 = p1->next;
            p2 = p2->next;
        }
        return true;
        
    }
};

