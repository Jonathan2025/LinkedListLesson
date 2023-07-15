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
# The current node starts off as the HEAD node



# So first we set up the main function which will just return the values and call the recursive helper function 
def linkedListValues(head):
    values = [] 
    current = head
    fillValuesHelper(current, values) # we call the recursive function here, what do we need ? The head and the values array
    return values

# So the helper function will be the recursive function, it should RECUSRIVELY traverse the values and append them to the array
def fillValuesHelper(current, values):
    # First what is the base case, what stops the traversal?
    if current is None:
        return 
    
    # Now if head is NOT null we should append the current head's values
    values.push(current.value)
    
    # NOW we make this recursive by calling our function again 
    fillValuesHelper(current.next, values)

    