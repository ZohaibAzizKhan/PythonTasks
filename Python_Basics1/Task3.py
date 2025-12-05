# Task 3: Given a string s, find the length of the longest substring without duplicate characters.
# function to find the length of the longest substring without duplicate characters
def longestLengthofsubstring(s):
  #  using sliding window technique
  # set to store unique characters
   seen=set()
  #  two pointers for the sliding window
  #  start and end
   start=0
  #  variable to store the maximum length of substring found
   maxLength=0
  #  iterating through the string using end pointer
   for end in range(len(s)):
      # if character at end pointer is already in the seen set
      while s[end] in seen:
        #  remove the character at start pointer from seen set
         seen.remove(s[start])
         start+=1
      seen.add(s[end])
      maxLength=max(maxLength,end-start+1)
   return maxLength
# Example1:
# Input: s = "abcabcbb"
# Output: 3
print(longestLengthofsubstring("abcabcbb"))  # Expected Output: 3
# Example2:
# Input: s = "bbbbb"
# Output: 1
print(longestLengthofsubstring("bbbbb"))     # Expected Output: 1