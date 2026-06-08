# Node class representing a train carriage
class Carriage:
    def __init__(self, carriage_no):
        self.carriage_no = carriage_no
        self.next = None


# Linked List class
class Train:
    def __init__(self):
        self.head = None

    # Add carriage at end
    def add_carriage(self, carriage_no):
        new_carriage = Carriage(carriage_no)

        if not self.head:
            self.head = new_carriage
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_carriage

    # Display train order
    def display(self):
        current = self.head

        while current:
            print(current.carriage_no, end="")
            if current.next:
                print(" -> ", end="")
            current = current.next
        print()

    # Reverse linked list
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_carriage = current.next
            current.next = prev
            prev = current
            current = next_carriage

        self.head = prev


# Main Program
train = Train()

train.add_carriage("Engine")
train.add_carriage("C1")
train.add_carriage("C2")
train.add_carriage("C3")
train.add_carriage("Guard")

print("Original Train Order:")
train.display()

train.reverse()

print("\nReversed Train Order:")
train.display()