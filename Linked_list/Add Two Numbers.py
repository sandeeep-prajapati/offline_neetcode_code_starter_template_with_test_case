class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
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
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print_list(add_two_numbers(l1, l2))  # Expected output: [7, 0, 8]
