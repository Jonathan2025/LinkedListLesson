# Write a function, linked_list_find, that takes in the head of a linked list and a target value. 
# The function should return a boolean indicating whether or not the linked list contains the targe


# Iterative Approach
# When we are at a current node we check its value to see if it matches the target value and then return 
# IF we dont find the target value when we reach the tail (null) then that means we can return false 

# Time: O(n) since we need to run through each node 
# Space: O(1) since we have a CONSTANT NUMBER of variables 

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def linked_list_find(head, target):
    current = head
    while current is not None: 
        if current.val == target:
            return True
        else:
            current = current.next # else if its not the target then move on to the next node
    
    # if we gone through the whole list without seeing a matching node, then return false 
    return False




# Recursive Approach 
# So we first make the recursive call on the first node 
# THEN we have 2 base cases 
# 1) if the current node value is equal to target then we can return true
# 2) if the current node value is null, then return false

# Time - O(N)
# Space - O(N) because each call we would need to store them in a call stack 


def linked_list_find(head, target):

    # we start with our two base cases
    if head is None:
        return False
    
    if head.val == target:
        return True
    

    # now if the first head node aint it, then we need to recusrively go through the rest of the nodes 
    # With recursion we need to get used to just calling the recursive function 
    return linked_list_find(head.next, target)


# Now of course the iterative solution is better since its better space complexity 

