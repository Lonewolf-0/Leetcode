/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNodes(ListNode* head) {
        ListNode* p = nullptr, *q = nullptr, *r = head;
        while(r){
            p = q;
            q = r;
            r = r->next;
            q->next = p;
        }
        ListNode* temp = q;
        while(p){
            if (temp->val > p->val){
                p = p->next;
                temp->next = p;
            }
            else if (temp->val < p->val){
                temp = p;
                p = p->next;
            }
            else if (temp->val == p->val){
                temp = p;
                p = p->next;
            }
        }
        
        r = q;
        p = nullptr;
        q = nullptr;
        while(r){
            p = q;
            q = r;
            r = r->next;
            q->next = p;
        }
        


        return q;

        
    }
};