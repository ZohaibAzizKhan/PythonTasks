# task using python regular expressions module
import re
def findMatches(text,pattern):
  #  this function returns True if the text matches the pattern else returns False
  # pattern may include '.' which matches any single character
  # and '*' which matches zero or more of the preceding element
   try:
      return re.fullmatch(pattern,text) is not None
   except re.error:
      return False
   
# Example usage:
print(findMatches('aa', 'a'))  # Output: False
# Example usage:
print(findMatches('aa', 'a*'))  # Output: True
# Example usage:
print(findMatches('ab', '.*'))  # Output: True
# Example usage:
print(findMatches('aab', 'c*a*b'))  # Output: True
# Example usage:
print(findMatches('mississippi', 'mis*is*p*.'))  # Output: False
# Example usage:
print(findMatches('aaa', 'a.a'))  # Output: True
# Example usage:
print(findMatches('aaa', 'ab*a*c*a'))  # Output: True