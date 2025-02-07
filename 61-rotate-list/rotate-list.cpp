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
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k==0) return head;
        int len =1 ;
        ListNode *p = head;
        while(p->next){
            len++;
            p = p->next;
        }
        // cout<<len;
        // cout<<p->val;
        p->next = head;

        k = k%len;
        k = len - k;
        p = head;
        for (int i=1; i<k; i++){
            p = p->next;
        }
        head = p->next;
        p->next = NULL;
        return head;

    }
};