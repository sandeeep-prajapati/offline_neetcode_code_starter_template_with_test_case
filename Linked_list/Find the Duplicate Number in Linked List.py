class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_duplicate(head):
    # Complete this function
    pass

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Test cases
head = create_linked_list([1, 3, 4, 2, 2])
print(find_duplicate(head))  # Expected output: 2

head = create_linked_list([3, 1, 3, 4, 2])
print(find_duplicate(head))  # Expected output: 3

head = create_linked_list([1, 1])
print(find_duplicate(head))  # Expected output: 1

head = create_linked_list([1, 1, 2])
print(find_duplicate(head))  # Expected output: 1
