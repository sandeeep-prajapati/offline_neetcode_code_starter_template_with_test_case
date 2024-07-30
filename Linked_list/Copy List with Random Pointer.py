class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random

def copy_random_list(head):
    # Complete this function
    pass

# Test cases
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1.random = None
node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

new_head = copy_random_list(node1)
# Expected to create a deep copy, you can write additional functions to verify deep copy if needed
