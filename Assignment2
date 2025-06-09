# Node class to represent each element in the list
class Node:
    def __init__(self, data):
        self.data = data  # value stored in the node
        self.next = None  # pointer to next node


# LinkedList class to manage the nodes
class LinkedList:
    def __init__(self):
        self.head = None  # start of the linked list

    # Add a new node at the end
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # if list is empty, make new_node the head
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node  # link last node to new node

    # Print the linked list
    def print_list(self):
        if self.head is None:
            print("List is empty.")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    # Delete the nth node from the list (1-based index)
    def delete_nth_node(self, n):
        try:
            if self.head is None:
                raise IndexError("Cannot delete from an empty list.")

            if n <= 0:
                raise ValueError("Index must be a positive integer.")

            if n == 1:
                print(f"Deleting node at position {n} with value {self.head.data}")
                self.head = self.head.next  # move head to next node
                return

            current = self.head
            count = 1
            while current is not None and count < n - 1:
                current = current.next
                count += 1

            if current is None or current.next is None:
                raise IndexError("Index out of range.")

            print(f"Deleting node at position {n} with value {current.next.data}")
            current.next = current.next.next  # skip the nth node

        except (IndexError, ValueError) as e:
            print("Error:", e)


# Testing the LinkedList
if __name__ == "__main__":
    ll = LinkedList()

    # Adding some values to the list
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)
    ll.add_node(50)

    print("Initial linked list:")
    ll.print_list()

    # Delete 3rd node (should be 30)
    ll.delete_nth_node(3)
    print("After deleting 3rd node:")
    ll.print_list()

    # Delete 1st node (should be 10)
    ll.delete_nth_node(1)
    print("After deleting 1st node:")
    ll.print_list()

    # Try deleting node at invalid position
    ll.delete_nth_node(10)

    # Try deleting from empty list
    new_list = LinkedList()
    new_list.delete_nth_node(1)
