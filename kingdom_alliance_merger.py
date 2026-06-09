class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head
        result = []

        while current:
            result.append(str(current.data))
            current = current.next

        return " -> ".join(result)


def merge_sorted_lists(head1, head2):
    dummy = Node(0)
    tail = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next

    if head1:
        tail.next = head1

    if head2:
        tail.next = head2

    return dummy.next


# Kingdom 1 Army
army1 = LinkedList()
for soldier in [1, 3, 5, 7, 9]:
    army1.append(soldier)

# Kingdom 2 Army
army2 = LinkedList()
for soldier in [2, 3, 6, 8, 10]:
    army2.append(soldier)

print("Kingdom 1 Army:")
print(army1.display())

print("\nKingdom 2 Army:")
print(army2.display())

# Merge armies
merged_head = merge_sorted_lists(army1.head, army2.head)

merged_army = LinkedList()
merged_army.head = merged_head

print("\nMerged Kingdom Alliance:")
print(merged_army.display())