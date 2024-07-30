class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    # Complete this function
    pass

# Test cases
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # Creates a cycle
print(has_cycle(head))  # Expected output: True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = head  # Creates a cycle
print(has_cycle(head))  # Expected output: True

head = ListNode(1)
print(has_cycle(head))  # Expected output: False
