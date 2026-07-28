# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # If there are 0, 1 or 2 nodes, no reordering is needed.
        if not head or not head.next or not head.next.next:
            return

        # -----------------------------
        # STEP 1 : Find the middle node
        # -----------------------------

        slow = head
        fast = head

        # slow moves 1 step, fast moves 2 steps
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Second half starts after middle
        second_half = slow.next

        # Break the list into two halves
        slow.next = None

        # -----------------------------
        # STEP 2 : Reverse second half
        # -----------------------------

        previous = None
        current = second_half

        while current:
            next_node = current.next      # Save next node
            current.next = previous       # Reverse pointer
            previous = current            # Move previous
            current = next_node           # Move current

        # 'previous' is now the head of reversed list
        second_half = previous

        # -----------------------------
        # STEP 3 : Merge both halves
        # -----------------------------

        first_half = head

        while second_half:

            # Save next nodes
            first_next = first_half.next
            second_next = second_half.next

            # Connect one node from first half
            first_half.next = second_half

            # Connect one node from second half
            second_half.next = first_next

            # Move forward
            first_half = first_next
            second_half = second_next