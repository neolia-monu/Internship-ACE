"""
    Singly LinkedList
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            traverse_node = self.root
            while traverse_node.next is not None:
                traverse_node = traverse_node.next
            traverse_node.next = Node(data)

    def delete(self, delete_data):
        if self.root is None:
            return False

        traverse_node = self.root
        prev_node = None
        while traverse_node is not None and traverse_node.data != delete_data:
            prev_node = traverse_node
            traverse_node = traverse_node.next
        
        if prev_node is None:
            self.root = traverse_node.next
            return True

        if prev_node is not None and traverse_node is not None:
            prev_node.next = traverse_node.next
            return True

        return False
        

    def search(self, searched_data):
        if self.root is None:
            return False
        
        traverse_node = self.root
        while traverse_node is not None:
            if traverse_node.data == searched_data:
                return True
            traverse_node = traverse_node.next
        
        return False
    
    def traversal(self):
        if self.root is None:
            return False

        tmp_node = self.root
        while tmp_node is not None:
            print(str(tmp_node.data) + "->", end=" ")
            tmp_node = tmp_node.next   



"""
  Create Object of the singly linked list
"""
node = SinglyLinkedList()


# add element
for n in range(1, 11):
    node.add(n)

# traverse the linked list
print(node.traversal())


"""
    Delete the node
"""
element = int(input("Enter delete element: "))
print("----------- Delete node", element ,"---------------")
print(node.delete(element))
print("--------------------------")

# search loop
for n in range(1, 11, 2):
    print(node.search(n))

"""
    Again traversal
"""
print(node.traversal())