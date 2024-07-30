class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    # Helper function to reverse a portion of the linked list
    def reverse(start, end):
        prev, curr = None, start
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy
    
    while True:
        # Find the k-th node
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next
        
        group_next = kth.next
        # Reverse the group
        prev, curr = kth.next, group_prev.next
        for _ in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to print the linked list
def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Test cases
head = create_linked_list([1, 2, 3, 4, 5])
print_list(reverse_k_group(head, 2))  # Expected output: [2, 1, 4, 3, 5]
head = create_linked_list([1, 2, 3, 4, 5])
print_list(reverse_k_group(head, 3))  # Expected output: [3, 2, 1, 4, 5]
