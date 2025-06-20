'''

Assignment 6-1
Problem: Reverse a Singly Linked List using Recursion - Choose your own list and reverse it recursively

 
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def reverse_list(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return new_head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original Linked List:")
print_list(head)

head = reverse_list(head)

print("Reversed Linked List:")
print_list(head)
