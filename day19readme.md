The Temperature Vault

A futuristic vault records temperature readings every second. The challenge is to instantly retrieve the minimum recorded temperature at any moment.

Approach

Two stacks are used:

Main Stack
Stores all temperature readings.
Min Stack
Stores only the minimum values encountered so far.

Whenever a new temperature is pushed:

If it is smaller than or equal to the current minimum, it is also pushed into the Min Stack.

Whenever a temperature is popped:

If the removed value is the current minimum, it is removed from the Min Stack as well.
Operations
Operation	Time Complexity
Push	O(1)
Pop	O(1)
Get Minimum	O(1)
Example
Push 34 → Min = 34
Push 29 → Min = 29
Push 41 → Min = 29
Push 22 → Min = 22
Push 18 → Min = 18

Pop 18 → Min = 22
Pop 22 → Min = 29
Real-World Applications
Server monitoring systems
Financial market tracking
Cloud infrastructure monitoring
Sensor data processing
Real-time analytics platforms