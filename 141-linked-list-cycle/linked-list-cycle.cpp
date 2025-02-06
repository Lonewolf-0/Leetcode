/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {

        ListNode *dummy = new ListNode();
        dummy->next = head;
        ListNode *s = dummy;
        ListNode *f = head;
        if (f==NULL || f->next == NULL ){
            return false;
        }
        if (f->next == head){
            return head;
        }

        while(s!=f){
            s= s == NULL ? head : s->next;
            f= f == NULL ? head : f->next->next;
            if (f==NULL || f->next == NULL ){
            return false;
            }
        }
        return s;

    }
};