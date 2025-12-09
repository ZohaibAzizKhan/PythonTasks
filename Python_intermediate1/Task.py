# Task: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# this function takes a string as input and returns True if the brackets are balanced, otherwise returns False
def find_opening_and_closing_brackets(s):
    # Dictionary to hold the mapping of closing and opening brackets
    bracketMap={
      ')':'(',
      '}':'{',
      ']':'['
          }
    # Stack to keep track of opening brackets
    stack=[]
    # Iterate through each character in the string
    for bracket in s:
      # If it's an opening bracket, push it onto the stack
      if bracket in bracketMap.values():
         stack.append(bracket)
        #  If it's a closing bracket, check for matching opening bracket
      elif bracket in bracketMap:
        #  check the stack is not empty
        # If stack is empty or top of stack doesn't match, return False
         if len(stack)==0:
            return False
        #  Pop the top element from the stack
         top=stack.pop()
        #  Check if the popped element matches the corresponding opening bracket
         if bracketMap[bracket] !=top:
            return False
    return len(stack)==0