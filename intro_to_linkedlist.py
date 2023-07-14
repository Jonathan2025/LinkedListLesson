#Linkedlist is made up of nodes that are LINKED

# A -> B -> C -> D --> Null
# Terminology A LINKS to B, B LINKS to C
# D links to NULL, D is the Tail node
# A node is the "HEAD"


# ----------------------- Linked List vs Array --------------------------------------

# So lets talk about why a linked list will be useful 
# linked list
# A -> B -> C -> D --> Null


# Array 
# Index   0 1 2 3 
# element a b c d


# Linked list is made of nodes while an array is made of elements 
# An array must be stored contigously in memory that means all elements are stored next to each other 
# Which means that operations using array may be more costly 

# Lets say we wanted to input "q" at 2, we want an insertion NOT a overwrite 
# For an array we need to SHIFT over a bunch of different elements in your array in order to then insert the new element 
# This will be very costly, O(n) insertion time complexity, where n is the number of nodes


# For linked list, the nodes dont need to be in memory and we DONT need any shifting 
# we just need to adjust the node's NEXT node. we just need to change 2 nodes 
# Time complexity is O(1) for an insertion

# ------------------------------------------------------------------------------------------
