class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#TODO: Write a function that takes in a list of values as an argument.
#TODO: The function should create a linked list containing each item of the list as the values of the nodes. 
#Constraints:

def algorithm(values):
    if len(values) == 1:
        return Node(values[0])
    if values:
        head = Node(values[0])
        curr = head
        for value in values[1:]:
            new_node = Node(value)
            curr.next = new_node
            curr = curr.next
        return head

    return None


list1 = algorithm([1, 7, 1, 8])




while list1:
    print(list1.val)
    list1 = list1.next




#NOTE: Left off at 03:40 on design requirements (system architecture)