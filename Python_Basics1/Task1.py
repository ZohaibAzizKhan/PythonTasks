# Task 1: Given a list of integers and a target integer, return the indices of the two numbers such that they add up to the target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# function for finding indices of two numbers that add up to target
# this function function accepts a list of integers and a target integer as input
# and returns a list containing the indices of the two numbers that add up to the target.
def indices_of_two_numbers(li,target):
  # iterating through the list to find the two numbers
  for i in range(len(li)):
    # checking if the sum of the current number and the next number equals the target
    if li[i]+li[i+1]==target:
      # returning the indices of the two numbers
      return [i,i+1]

# example usage
# defining a list of integers and a target integer
nums=[2,7,11,15]
target=26
print(indices_of_two_numbers(nums,target))