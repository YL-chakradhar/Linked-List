class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create the head node with value 10
head = Node(10)
currentnode = head

# Build the linked list with values from 2 to 9
for i in range(2, 10):
    newnode = Node(i)
    currentnode.next = newnode  # Link the new node to the current node
    currentnode = newnode       # Update the current node to the new node

# Define the target value to remove
target_value = 5

# Special case: if the head itself is the target value
if head.data == target_value:
    head = head.next  # Move head to the next node
else:
    # Traverse the list to find the node with the target value
    temp = head
    prev = None
    while temp is not None:
        if temp.data == target_value:
            break
        prev = temp
        temp = temp.next
    
    # If the target value is found
    if temp is not None:
        prev.next = temp.next  # Skip the node with the target value

# Reinitialize currentnode to the head of the list
currentnode = head

# Traverse and print the updated linked list
while currentnode is not None:
    print(currentnode.data, end="")
    if currentnode.next is not None:
        print("->", end="")
    currentnode = currentnode.next
