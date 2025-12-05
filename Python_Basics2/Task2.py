#Task 2 Function to convert an integer to Roman numeral representation
# The function takes an integer as input and returns a string representing the Roman numeral.
# Roman numerals are represented by combinations of letters from the Latin alphabet.

def covert_to_roman_symbols(number):
# Dictionary mapping integer values to their corresponding Roman numeral symbols
  roman_dict={
    1000:'M',
    900:'CM',
    500:'D',
    400:'CD',
    100:'C',
    90:'XC',
    50:'L',
    40:'XL',
    10:'X',
    9:'IX',
    5:'V',
    4:'IV',
    1:'I'
  }
  # Variable to store the resulting Roman numeral string
  result=""
  # Iterate through the dictionary items
  # For each integer value and its corresponding Roman symbol
  # subtract the integer value from the number
  # and append the Roman symbol to the result string
  for num_value,symbol in roman_dict.items():
    while number >= num_value:
      result+=symbol
      number-=num_value
      # Check if the number has been reduced to zero
      if number==0:
        break
      # Additional check to break the outer loop for optimization
    if number==0:
      break
    # Additional check to break the outer loop for optimization
  return result
# Example Usage
# Input: number = 3
# Output: "III"
print(covert_to_roman_symbols(3))    # Expected Output: III
# Input: number = 58
# Output: "LVIII"
print(covert_to_roman_symbols(58))   # Expected Output: LVIII
# Input: number = 1994
# Output: "MCMXCIV"
print(covert_to_roman_symbols(1994))  # Expected Output: MCMXC
