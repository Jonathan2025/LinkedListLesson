# Write a function, zipper_lists, that takes in the head of two linked lists as arguments.
# The function should zipper the two lists together into single linked list by alternating nodes. 
# If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. 
# The function should return the head of the zippered linked list.

# Pretty much we merge these 2 lists and they need to alternate 

# A --> B --> C --> D --> E -- > F
# Q --> R


# Iterative Approach
# n = length of list 1 
# m = length of list 2
# Time O(min(n,m)) # this is because we only need to iterate through one list and then we just take on the remainder thats why its the shorter of the 2 lists
# Space: O(1) we use a fixed number of variables and also we arent creating any new nodes just shifting pointers


# First we need current pointers - one for list 1 and one for list 2 AND we need to track the tail of the merged output list
# We then can create a counter variable 

# So pretty much we add the first node from list one. When we have a count that is EVEN we take a node from list 2, otherwise we take it from 
# List 1. Also make sure we UPDATE the current pointer so we need to move up 

# When we reach the end of one list, then we just add the rest of the nodes from the other list




# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def zipperLists(head1, head2):
    outputTail = head1 # we want to intialize the output list, think about what we need to return 
    current1 = head1
    current2 = head2

    count = 0 # we also need a counter to see if we are odd or even and this will tell us which list to take from 



    while (current1 and current2): # we dont want either to be null 
        if count % 2 == 0:  
            # if we are even then take from list 2
            outputTail.next = current2.next # add to the output tail
            current2 = current2.next # make sure to update the pointer
        else: 
            outputTail.next = current1.next 
            current1 = current1.next



        tail = tail.next # then we ALSO need to update the pointers
        count += 1 # after we append to the output tail we need to increment the count 


    # lets say one of the list is now empty, then we need to add the rest of the remaining list 
    if current1 is not None:
        outputTail.next = current1
    
    if current2 is not None: 
        outputTail.next = current2 
    


    # Think about what we need to return 
    return outputTail





# Recursive Approach 
def zipperLists(head1, head2):

    # Base case when do we stop 
    if head1 is None and head2 is None:
        return None 
    

    # What is one of them is null, then just return the remainder of the other one - how to deal with remainder nodes
    if head1 is None: 
        return head2 
    if head2 is None: 
        return head1 
    

    # Now the next part is using recursive function 
    # important to note is creating temporary variables before you overwrite'
    # So we do this for the head1 and head2 pointers
    next1 = head1.next
    next2 = head2.next

    #Now we need to set the next pointers 
    head1.next = head2
    head2.next = zipperLists(next1, next2)






    return head1 


# So first we set a to Head1 and then b as next 1

# A ---> B ---> C
# H1     N1

# X ---> Y ---> Z
# H2     N2


# So we ARENT creating any new nodes 
# We start with head1 which is A, but we set the head1.next as head2 which is X
# A--> X

# THEN we set head2's next as the recursive call