# function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string.
def longestPrefix(strList):
  # initially assuming the first string as the prefix
  prefix=strList[0]
  # iterating through the list of strings starting from second string
  for index in range(1,len(strList)-1):
    # comparing the current prefix with each string
    current_string=strList[index]
    # finding the common prefix between the current prefix and the current string
    j=0
    while j<len(prefix) and j<len(current_string):
      # if characters do not match, break the loop
      if prefix[j]!=current_string[j]:
        break
      # if characters match, move to the next character
      j+=1
    prefix=prefix[:j]
  return prefix
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
print(longestPrefix(["flower","flow","flight"]))  # Expected Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
print(longestPrefix(["dog","racecar","car"]))     # Expected Output: ""
# Example 3:
# Input: strs = ["interspecies","interstellar","interstate"]
# Output: "inters"
print(longestPrefix(["interspecies","interstellar","interstate"]))  
