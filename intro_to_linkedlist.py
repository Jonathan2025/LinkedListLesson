#Linked list is made up of nodes that are LINKED

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
# Traversing a Linked List
# This mean we vist every node to perform some operation on the nodes 
# We need a few variables 
# Current Node


#       A ->       B       ->     C ->     D --> Null
# current    current.next 

# We can stop the algo when current is equal to NULL


# ------------------------------------------------------------------------------------------
# Building a linked list 
# First we need the node class 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



# Then we can create some instances 
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")


# How can we put together to a linked list 
a.next = b
b.next = c
c.next = d
# A -> B -> C -> D --> Null


# ------------------------------------------------------------------------------------------
# Now lets try to traverse the linked list ITERATIVELY
def printLinkedList(head):
    # Main idea - we need to consistently update a current pointer
    
    current = head # FIRST initialize our current pointer as the head

    # how much do we run this algorithm, do it while current pointer isnt equal to null 
    while current is not None:
        print(current.value)
        # NOW dont forget we also need to UPDATE current node 
        current = current.next

print("This is the Iterative Way")
printLinkedList(a) # this will print out A, B, C, D


# What if we did the while loop as "while current.next is not None"
# Then we would actually get one less 
# this will print out A, B, C and NOT including D 

# ------------------------------------------------------------------------------------------
# Now lets try to traverse the linked list RECURSIVELY
def printLinkedListRec(head):

    # FIRST we start with base case, we can ask ourselves, WHEN are we done with the algorithm? When head is null
    if head is None: 
        return 
    
    # Now if the head is not null, then we can just print out the value 
    print(head.value)

    # IMPORTANT - we need to make a RECURSIVE call here by calling the same function 
    printLinkedListRec(head.next) # what do we pass as an argument? we pass the next node



    