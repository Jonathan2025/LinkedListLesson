# Write a function, get_node_value, that takes in the head of a linked list and an index. 
# The function should return the value of the linked list at the specified index.

# ITERATIVE Approach 
# Pretty much we have a target index and we need a count varaible 
# Each time we traverse to the next node we increment the count 
# Once the count variable is equal to the target and then return the node value 
# So we are basically counting down

# Time O(N)
# Space O(1)

def get_node_value(head, index):

    current = head 
    count = 0
    while current is not None: 
        if count == index: # referring to if the count equals the target index
            return current.val
        
        count += 1
        current = current.next 
    
    # NOW dont forget what if we get to the end, just return null
    return None






# Recursive Approach 
# This one is a bit confusing but for the recusrive approach we start at the head node and so it will take the target index and then we count down 
# from that first node 
# so lets say this is our linked list 
# A -> B -> C -> D --> Null
# we start A as 2, then B as 1, then C as 0, and then now C's value is the one we want to return 

# Time O(N)
# Space O(N)


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def get_node_value(head, index):

    # We picture starting at the head node
    # lets start with the base case, if we hit a null node then just return null cuz it doesnt have a value 
    if head is None:
        return None
    
    # the other base case is if we found the right index 
    if index == 0: 
        return head.val
    

    # if neither are true then call the recursive function on the next node 
    return get_node_value(head.next, index -1)