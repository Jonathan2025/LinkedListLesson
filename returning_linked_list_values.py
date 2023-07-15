# Returning Linked List Values 
# We are given a linked list and we need to return the values of the nodes


# linked list
# A -> B -> C -> D --> Null

# OVERALL Pattern
# First we need to start a current variable, set it to the head 
# Then create a VALUES array to append values to 
# Now set the current variable to next 
# Continue traversing until curreNT goes to null 


# ----------------------------------------------------------------------------------------
# Iterative Solution 

# n  = Number  of nodes
# Time : O(N)
# Memory: O(N)


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



def linkedListValues(head): 
    values = [] # we do need a list of values that will be added
    current = head 
    while current is not None: # TIP when we write our conditions, we wants to try to stick with "current" and NOT "current.val"
        # this is so that things dont become chunky 
        values.push(current.val) # append the value of the node
        current = current.next  # then move to the next node
    
    # once we have all the values return them 
    return values 


# ----------------------------------------------------------------------------------------
# Recursive solution 
# Slightly confusing but The way to do this is that we have to call a "Helper Function"

# So first we set up the main function which will just return the values and call the recursive helper function 
def linkedListValues(head): 
    values = [] # we do need a list of values that will be added
    fillValues(head, values) # this is the call to the helper function 
    return values 


# Now lets create the helper recursive function
def fillValues(head, values): 
    # First start with the base case, which is if the node becomes null then we stop
    if head is None:
        return 
    
    # Now what if the head is NOT null 
    values.push(head.value)

    # Now we could also have remaining nodes 
    fillValues(head.next, values) # IMPORTANT this is what makes something recursive, we call its function again 