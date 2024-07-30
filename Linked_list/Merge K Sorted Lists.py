class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    # Complete this function
    pass

# Helper function to print the linked list
def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Test cases
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
print_list(merge_two_lists(l1, l2))  # Expected output: [1, 1, 2, 3, 4, 4]
