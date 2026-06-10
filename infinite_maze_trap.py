class MazeNode:
    def __init__(self, path_id):
        self.path_id = path_id
        self.next = None


def detect_cycle(start):
    slow = start
    fast = start

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# -------------------------------
# Maze 1: No Cycle
# -------------------------------
path1 = MazeNode("A")
path2 = MazeNode("B")
path3 = MazeNode("C")
path4 = MazeNode("D")

path1.next = path2
path2.next = path3
path3.next = path4

print("Maze 1 Cycle Detected:", detect_cycle(path1))

# -------------------------------
# Maze 2: Contains Cycle
# -------------------------------
room1 = MazeNode("X")
room2 = MazeNode("Y")
room3 = MazeNode("Z")
room4 = MazeNode("W")

room1.next = room2
room2.next = room3
room3.next = room4
room4.next = room2  # Creates cycle

print("Maze 2 Cycle Detected:", detect_cycle(room1))

# -------------------------------
# Maze 3: Single Node Cycle
# -------------------------------
single = MazeNode("Solo")
single.next = single

print("Maze 3 Cycle Detected:", detect_cycle(single))