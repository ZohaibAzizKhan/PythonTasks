#Task 1 Function to check if a number is a palindrome
# A palindrome is a number that remains the same when its digits are reversed.
# This function takes an integer as input and returns True if it is a palindrome, otherwise False.
def isPalindrome(number):
  temp=number
  # Variable to store the reversed number
  reverse=0
  # Variable to store the remainder
  reminder=0
  # Reversing the number
  while temp != 0:
    # Extracting the last digit of the number
    reminder=temp%10
    # Building the reversed number
    reverse=(reverse*10)+reminder
    # Removing the last digit from the number
    temp=temp//10
  # Checking if the reversed number is equal to the original number
  return number==reverse


# Example Usage
# Input: num = 121
# Output: True
num=121
print(isPalindrome(num))
# Input: num = -123
# Output: False
num=123
print(isPalindrome(num))
# Input: num = 12321
# Output: True
num=12321
print(isPalindrome(num))