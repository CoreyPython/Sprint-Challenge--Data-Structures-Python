
from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # Assigning the capacity to the input property.
        self.current = None # Starting out with None.
        self.storage = DoublyLinkedList() # Using a DLL as the storage container.

    def append(self, item):
        if self.storage.length < self.capacity: # Checking the length of the Storage (DLL) and comparing to the Capacity input.
            self.storage.add_to_tail(item) # If the storage has room we are adding it to it. (Not at capacity)
            self.current = self.storage.tail # Assigning the most current item from the tail that we just added.
            return
        else:
            if self.current == self.storage.tail: # If the current value is the same as the tail..
                self.current = self.storage.head # We are assigning it to the head instead.
            else:
                self.current = self.current.next # We are assigning it to the current.next
            self.current.value = item # Then we are taking the item and adding it to be to equal to the current value.

    def get(self):
        contents = [] # Creating a list (Array)

        node = self.storage.head # Creating a Node and giving it the head value.
        while node is not None: # While the Node is not empty,
            contents.append(node.value) # We are adding the node's value to the array
            node = node.next # We are assigning the node to the next
        return contents # Returning the array of contents.