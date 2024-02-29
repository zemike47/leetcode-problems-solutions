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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
   
        ListNode* head1 = l1;
        ListNode* head2 = l2;
        ListNode* sumHead = NULL;
        ListNode* tail = NULL; // to keep track of the tail of the result list
        int carry = 0;

        while (head1 != NULL || head2 != NULL || carry != 0) {
            int val1 = (head1 != NULL) ? head1->val : 0;
            int val2 = (head2 != NULL) ? head2->val : 0;

            int sum = val1 + val2 + carry;
            carry = sum / 10;

            ListNode* newNode = new ListNode(sum % 10);

            if (sumHead == NULL) {
                sumHead = newNode;
                tail = newNode;
            } else {
                tail->next = newNode;
                tail = newNode;
            }

            if (head1 != NULL) head1 = head1->next;
            if (head2 != NULL) head2 = head2->next;
        }

        return sumHead;
    }

};