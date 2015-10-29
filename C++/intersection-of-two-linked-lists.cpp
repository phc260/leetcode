tion for singly-linked list.
 * struct ListNode {
 *  *     int val;
 *   *     ListNode *next;
 *    *     ListNode(int x) : val(x), next(NULL) {}
 *     * };
 *      */
class Solution {
private:
    int len(ListNode *head) {
        int c = 0;
        while(head) {
            ++c;
            head = head->next;
        }
        return c;
    }
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int len_a = len(headA);
        int len_b = len(headB);
        while(len_a>len_b) {
            headA = headA->next;
            --len_a;
        }
        while(len_b>len_a) {
            headB = headB->next;
            --len_b;
        }
        while(headA!=headB){
            headA = headA->next;
            headB = headB->next;
        }
        return headA;
    }
};

