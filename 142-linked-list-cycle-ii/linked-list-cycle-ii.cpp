class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *slow = head, *fast = head, *entry = head;
        
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) break;
        }
        
        if (!fast || !fast->next) return nullptr;
        
        while(slow != entry){
            entry = entry->next;
            slow = slow->next;
        }
        return slow;
    }
};
