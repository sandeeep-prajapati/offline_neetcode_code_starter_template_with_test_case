class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
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
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reorder_list(head)
print_list(head)  # Expected output: [1, 5, 2, 4, 3]
