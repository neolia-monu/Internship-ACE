"""
    Singly LinkedList
"""

class SinglyLinkedList():

    def __init__(self, data):
        self.data = data
        self.next = None

    def add(self, data, root):
        cur = root
        while cur.next != None:
            cur = cur.next
        cur.next = SinglyLinkedList(data)

    def delete(self, data, root):
        
        if root == None:
            return None

        cur = self.search(data, root)
        if cur is not None:
            cur.next = cur.next.next
            return True
        
        return False
        

    def search(self, data, root):
        cur = root
        if cur is None:
            return None
        
        # edge case
        if cur.data == data:
            print("--- Data Found ---")
            return cur
        
        while cur != None and cur.next != None:
            if cur.next.data == data:
                print("--- Data Found ---")
                return cur
            cur = cur.next
        
        print("--- Not Found ---")
        return None
    
    def traversal(self, root):
        if root is None:
            print("Nothing to traverse")
            return
        cur = root
        while cur.next != None:
            print(str(cur.data) + "->", end=" ")
            cur = cur.next
        print(cur.data)
        

head = SinglyLinkedList(0)
cur = head
n = 2
for n in range(1, 11):
    cur.add(n, head)
    n += 1

cur.traversal(head.next) # traveral
cur.search(2, head)  # Data Found
cur.search(12, head)  # Data Not Found


"""
    Delete the node 8
"""
print("----------- Delete node 8 ---------------")
print(cur.delete(8, head))
print("--------------------------")

# search loop
for n in range(1, 11):
    # print(n)
    cur.search(n, head)