class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    # Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove nth node from end
    slow.next = slow.next.next

    return dummy.next


def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# Example Message Chain
head = ListNode("MSG1")
head.next = ListNode("MSG2")
head.next.next = ListNode("CORRUPTED")
head.next.next.next = ListNode("MSG4")
head.next.next.next.next = ListNode("MSG5")

print("Original Chain:")
print_list(head)

n = 3  # Remove 3rd message from end

head = removeNthFromEnd(head, n)

print("\nDecoded Chain:")
print_list(head)