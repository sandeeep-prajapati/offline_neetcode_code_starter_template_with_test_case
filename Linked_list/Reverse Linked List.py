class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
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
print_list(reverse_list(head))  # Expected output: [5, 4, 3, 2, 1]
