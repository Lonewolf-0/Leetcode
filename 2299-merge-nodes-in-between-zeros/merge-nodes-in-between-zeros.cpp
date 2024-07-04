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
    ListNode* mergeNodes(ListNode* head) {
        ListNode *i, *j;
        i = head->next;
        j = head->next;
        int sum = 0;
        while(j){
            if(j->val == 0 ){
                
                i->val = sum;
                i->next = j->next;
                i=j->next;
                sum=0;
            }
            else{
                sum+=j->val;
            }
            // cout<<sum<<" ";
            
            j=j->next;
        }
        return head->next;
    }
};