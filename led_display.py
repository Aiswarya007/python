user = input("Enter number: ")

segments = [
    ['###', '# #', '# #', '# #', '###'],  # 0
    ['  #', '  #', '  #', '  #', '  #'],  # 1
    ['###', '  #', '###', '#  ', '###'],  # 2
    ['###', '  #', '###', '  #', '###'],  # 3
    ['# #', '# #', '###', '  #', '  #'],  # 4
    ['###', '#  ', '###', '  #', '###'],  # 5
    ['###', '#  ', '###', '# #', '###'],  # 6
    ['###', '  #', '  #', '  #', '  #'],  # 7
    ['###', '# #', '###', '# #', '###'],  # 8
    ['###', '# #', '###', '  #', '###']   # 9
]

# Initialize a list to store the lines for each row of the output
output_lines = [""] * 5

# Iterate through each digit in the user input
for digit in user:
    if digit.isdigit():  # Check if the character is a digit
        digit = int(digit)
        if 0 <= digit <= 9:  # Ensure the digit is within the valid range
            for i in range(5):  # Iterate through each row of the segments
                output_lines[i] += segments[digit][i] + " "  # Concatenate segments with space

# Print each row of the output
for line in output_lines:
    print(line)
