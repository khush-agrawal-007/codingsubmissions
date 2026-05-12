# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if not list1 and not list2: return
        # if not list1: return list2
        # if not list2: return list1
        # if list1.val<=list2.val:
        #     nxt=list1.next
        #     list1.next=self.mergeTwoLists(nxt,list2)
        #     return list1
        # else:
        #     nxt=list2.next
        #     list2.next=self.mergeTwoLists(list1,nxt)
        #     return list2
        d = ListNode()
        curr = d

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        
        curr.next = list1 if list1 else list2
        return d.next












# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna