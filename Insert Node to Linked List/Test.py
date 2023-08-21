class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

#TODO: Insert a new node with the value into the list at the specified index
#Constraints: You may assume that the input list is non-empty

def algorithm(list1, value, insert_index):
    if insert_index == 0:
        new_node = Node(value)
        new_node.next = list1
        return new_node

    curr = list1
    index = 1
    while curr:
        if insert_index == index:
            new_node = Node(value)
            following_node = curr.next
            curr.next = new_node
            new_node.next = following_node
            return list1
        index += 1
        curr = curr.next

list1 = algorithm(a, 'x', 2)

while list1:
    print(list1.val)
    list1 = list1.next




#NOTE: Left off at 03:40 on design requirements (system architecture)