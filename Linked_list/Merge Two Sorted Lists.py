import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    # Create a min-heap to keep track of the smallest elements from each list
    min_heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))
    
    # Create a dummy head for the result list
    dummy = ListNode()
    current = dummy
    
    # Process the heap until it is empty
    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        current.next = ListNode(val)
        current = current.next
        node = node.next
        if node:
            heapq.heappush(min_heap, (node.val, i, node))
    
    return dummy.next

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
list1 = create_linked_list([1, 4, 5])
list2 = create_linked_list([1, 3, 4])
list3 = create_linked_list([2, 6])
print_list(merge_k_lists([list1, list2, list3]))  # Expected output: [1, 1, 2, 3, 4, 4, 5, 6]
