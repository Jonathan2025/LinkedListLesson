# Reverse Linked List 
# Write a function, reverse_list, that takes in the head of a linked list as an argument. 
# The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.


# linked list
# A -> B -> C -> D --> Null

# Appraoch 
# So first we have a current node. Of course the current node will start at the Head node. 
# All we do is point current node to previous node
# But at the same time we must SAVE current.next
# Once we get to current is null then we are done 

# Iterative 
# Time O(N)
# Space O(1) constant number of variables


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def reverse_list(head):
    # first we need our variables to start
    previous = None
    current = head 
    if current is not None:
        next = current.next # save the next variable as a temp variable
        current.next = previous # we need to shift the order of the nodes
        previous = current 
        current = next 




# Beginning before we traverse we pretty much just set up prev, current and next
# Null --> A   ->   B         -> C -> D --> Null
# prev    Curr   Curr.next


# First iteration 
# Null <-- A   ->   B         -> C -> D --> Null
# We need to also do next = current.next so that we dont lose that variable while shifting things around 
# first we do current.next is previous <--

#then we do previous = current and current = next
# Null <-- A   ->   B         -> C -> D --> Null
#          prev    Curr   Curr.next








# Recursive Solution 
def reverse_list(head, previous = None): # set a default to None if the user doesnt provide a head
    if head is None: 
        return previous
    next = head.next
    head.next = previous 
    return reverse_list(next, head)


# so pretty much the recursive solution is being translated from the iterative solution 
# previous first starts as Null 
# head.next becomes previous 
# then we call the function recursively, where head/ current becomes next and then the previous becomes head 
























# A -> B -> C -> D --> Null












