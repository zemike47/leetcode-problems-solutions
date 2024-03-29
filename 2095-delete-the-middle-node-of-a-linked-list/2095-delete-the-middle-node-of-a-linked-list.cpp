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
    ListNode* deleteMiddle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* beforeSlow = NULL;
        
        while(fast!= NULL && fast->next != NULL){
           fast= fast->next->next;
            beforeSlow = slow;
            slow = slow->next;
            
        }
        if(beforeSlow != NULL){
            beforeSlow->next = slow->next;
        }else{
            head = slow->next;
        }
        
        delete slow;
        
        return head;
    }
};