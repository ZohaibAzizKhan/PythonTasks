# task 2 You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
#  and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
import math

# first of all lets create a simple linked list class which stores current value and address to next node
class Node:
  # The constructor initializes a node with a value (default 0) and a pointer to the next node (default None).
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  # This method performs the addition of the two linked lists.
  def twoSum(self, linkedList1, linkedList2):
    # Initialize a dummy head node. This is a common technique to simplify list creation, 
    # as we can start appending nodes to `dummy_head.next`.
    dummy_head = Node(0)
    # `current` will be the pointer that moves along the resulting list, appending new nodes.
    current = dummy_head
    # Initialize the carry to 0.
    carry = 0
    
    # Loop continues as long as there are digits left in either list OR there is a remaining carry.
    while linkedList1 or linkedList2 or carry:
      # Get the value from the current node of linkedList1. If lindkedList2 is exhausted, use 0.
      val1 = linkedList1.val if linkedList1 else 0
      # Get the value from the current node of linkedList1. If linkedList is exhausted, use 0.
      val2 = linkedList2.val if linkedList2 else 0
      
      # Calculate the total sum for the current position: val1 digit + val2 digit + previous carry.
      sum_val = val1 + val2 + carry
      
      # Calculate the new carry (the "tens" place).
      carry = sum_val // 10
      
      # Calculate the digit for the new node (the "ones" place).
      digit = sum_val % 10
      
      # Create a new node with the calculated digit.
      current.next = Node(digit)
      # Move the result pointer forward to the newly created node.
      current = current.next
      
      # Move the linkedList1 pointer to the next node if it is not null.
      if linkedList1:
        linkedList1 = linkedList1.next
      # Move the linkedList pointer to the next node if it is not null.
      if linkedList2:
        linkedList2 = linkedList2.next
        
    # The result list is the node immediately following the dummy head.
    return dummy_head.next
    
  # Helper method to convert a standard list of digits into a linked list.
  # This implementation creates a linked list where the digits are in the same order as the input list.
  def List_to_Linked_list(self, li):
    # Initialize a dummy head for the list creation.
    dummy_head = Node(0)
    # Store the address of the current node pointer.
    current = dummy_head
    
    # Iterate through the input list of digits.
    for i in li:
      # Create a new node for the current digit.
      current.next = Node(i)
      # Move the pointer to the new node.
      current = current.next
      
    # Return the head of the new linked list (skipping the dummy node).
    return dummy_head.next

  # Helper method to convert a linked list back to a standard list for easy printing.
  def Linked_list_to_list(self, head):
    result = []
    current = head
    # Traverse the linked list until the end.
    while current:
      # Append the value of the current node to the result list.
      result.append(current.val)
      # Move to the next node.
      current = current.next
      
    return result[::-1]

solver = Solution()

# Example 1: Large numbers
# [5,4,3,2,1] + [5,6,7,6,4] = [1,1,1,0,8,5]
li1_to_linkedList = solver.List_to_Linked_list([1, 2, 3, 4, 5])
li2_to_linekedList = solver.List_to_Linked_list([4, 6, 7, 6, 5])

# Example 2: Classic problem example
# Input: [3,4,2] + [4,6,5] = [8,0,7]
l1 = solver.List_to_Linked_list([2, 4, 3])
l2 = solver.List_to_Linked_list([5, 6, 4])

# Perform the addition for Example 1.
result = solver.twoSum(li1_to_linkedList, li2_to_linekedList)
# Perform the addition for Example 2.
result1 = solver.twoSum(l1, l2)

# Print the results after converting the output linked list back to a readable number list.
print(solver.Linked_list_to_list(result))   # Expected Output: [1, 1, 1, 0, 8, 5] (111085)
print(solver.Linked_list_to_list(result1))  # Expected Output: [8, 0, 7] (807)
