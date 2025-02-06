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
        

        while(s!=f){
            if (f==NULL || f->next == NULL ){
            return false;
            }
            s= s == NULL ? head : s->next;
            f= f == NULL ? head : f->next->next;
            
        }
        return s;

    }
};