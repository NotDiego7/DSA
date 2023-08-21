class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = Node("h")
node2 = Node("i")
node3 = Node("j")
node4 = Node("i")

node1.next = node2
node2.next = node3
node3.next = node4


#TODO: Remove only the first instance of target value AND redirect node.next
#

def algorithm(list1, target):
    prev = None
    curr = list1

    if curr.val == target:
        return curr.next

    while curr:  
        if curr.val == target:
            prev.next = curr.next
            return list1
        prev = curr
        curr = curr.next

list1 = algorithm(node1, "i")
while list1:
    print(list1.val)
    list1 = list1.next

#TODO: Left off at 03:40 on design requirements (system architecture
#NOTE: ...