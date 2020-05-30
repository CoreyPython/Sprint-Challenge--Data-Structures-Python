class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if not node: # Checking to see if there is a node.
            return None # Return None if it is empty
        if node.next_node is None: # Checking to see if the next Node is empty.
            return node # Returning the node if it is.
        head = node # The head is the node
        new_head = head.next_node # The new head is the next node in line.
        future_head = self.reverse_list(new_head, None) # We are setting the future head to the next head in line recursivly.
        new_head.next_node = head # we assign the new head's next node as the head
        new_head = future_head # we are setting the new head from the value of the Future head.
        self.head = new_head # Setting the self.head's value from the new head.
        return new_head # Returning the new head. 
