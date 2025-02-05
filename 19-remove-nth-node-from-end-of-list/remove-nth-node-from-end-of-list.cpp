class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0); 
        dummy->next = head;
        ListNode *slow = dummy, *fast = dummy;
        for (int i = 0; i < n; ++i) { 
            fast = fast->next;
        }
        while (fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next;
        }
        
        ListNode* temp = slow->next;
        slow->next = slow->next->next;
        delete temp;
        
        return dummy->next; // Correctly returns new head
    }
};
