class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#   999
#  +  6
#  ----
#  1005

a1 = Node(9)
a2 = Node(9)
a3 = Node(9)
a1.next = a2
a2.next = a3
# 9 -> 9 -> 9

b1 = Node(6)
# 6

# Result: 5 -> 0 -> 0 -> 1

#TODO: Write a function that takes in the head of two linked lists, each representing a number. 
#TODO: The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed
#TODO: The function should return the head of a new linked list representing the sum of the input lists reversed.

def algorithm(list1, list2):
    first_num = ""
    second_num = ""
    
    while list1:
        first_num = str(list1.val) + first_num
        list1 = list1.next

    while list2:
        second_num = str(list2.val) + second_num
        list2 = list2.next

    sum_total = int(first_num) + int(second_num)
    sum_total = str(sum_total)
    # ---------------------------------------------------------------------------- #
    new_node = Node(None)
    head = new_node
    for i in sum_total[::-1]:
        curr = Node(int(i))
        new_node.next = curr
        new_node = new_node.next
    return head.next



list1 = algorithm(a1, b1)




while list1:
    print(list1.val)
    list1 = list1.next