from collections import deque


class ThemeParkFastPassSimulator:
    def __init__(self):
        self.vip_queue = deque()
        self.normal_queue = deque()

    def add_visitor(self, name, is_vip=False):
        if is_vip:
            self.vip_queue.append(name)
            print(f"⭐ VIP Visitor Added: {name}")
        else:
            self.normal_queue.append(name)
            print(f"👤 Normal Visitor Added: {name}")

    def process_visitor(self):
        if self.vip_queue:
            visitor = self.vip_queue.popleft()
            print(f"🎢 Processing VIP Visitor: {visitor}")
        elif self.normal_queue:
            visitor = self.normal_queue.popleft()
            print(f"🎢 Processing Normal Visitor: {visitor}")
        else:
            print("❌ No visitors waiting.")

    def display_queues(self):
        print("\n--- Current Queue Status ---")
        print("VIP Queue   :", list(self.vip_queue))
        print("Normal Queue:", list(self.normal_queue))
        print("----------------------------\n")


# Driver Code
park = ThemeParkFastPassSimulator()

# Adding Visitors
park.add_visitor("Alice")
park.add_visitor("Bob")
park.add_visitor("Charlie", True)
park.add_visitor("David")
park.add_visitor("Eva", True)

park.display_queues()

# Processing Visitors
park.process_visitor()
park.process_visitor()
park.process_visitor()

park.display_queues()