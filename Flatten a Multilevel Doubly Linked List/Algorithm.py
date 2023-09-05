"""
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, 
and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, 
also containing these special nodes. These child lists may have one or more children of their own, and so on, 
to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, 
doubly linked list. Let curr be a node with a child list. 
The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.
"""

#TODO: The nodes in the list must have all of their child pointers set to null
#TODO: Return the head of the flattened list.
#TODO: 

n = 5
# --------------------------------- First Try -------------------------------- #

def algorithm():
    if head:
        curr = head
        pending_node = []
        
        while curr.next:

            if curr.child: #Flatten Logic
                pending_node.append(curr.next)
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
            curr = curr.next #Move forward a node

        for i in range(len(pending_node)):
            curr.next = pending_node.pop()
            while curr.next:
                curr.next.prev = curr
                curr = curr.next #Move forward a node
                
        return head
    
    return None


print(algorithm())


# O(n * b) Time complexity 84.98% | O(n) Space complexity Beats 65.29%