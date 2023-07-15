# Sum List Problem 
# Write a function sumList that takes in the head of a linked list containing numbers numbers as an argument 
# The function should return the total sum of all values in the linked list 

# Pattern 
# We will pretty much traverse the linked list and then accumulate the sum 

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#ITERATIVE Solution 
# N = number of nodes 
# Time complexity: O(N) iterating through each node
# Space: O(1) because we just need a current node and the sum variable 

def sumList(head):
    sum = 0 # initialize a sum variable 
    current = head 
    while current is not Null:
        sum += current.value

        # remember we also need to update the current node 
        current = current.next
    
    return sum 



# Recursive Solution 
# N = number of nodes 
# Time complexity: O(N) iterating through each node
# Space: O(N) because we need to call the recursive function on each node. We have to call every recusrive function onto the call stack

# Lets think about our base case - when the current node is null, we can just return 0 because its NOT adding to the sum 
# THEN we "RETURN BACK" to the previous nodes 

def sumList(head):

    # we start with the base case --> which is if there are no nodes then the sum is 0 
    if head is None:
        return 0


    # Now lets say the node is not null. Then we need to get the current node value and then add it to the next recursive call 
    return head.val + sumList(head.next)