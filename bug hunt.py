# Bug Hunt

count = 1
total = 0

# BUG: Missing colon at end of while line. Python needs : to start the loop block.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Original code was while count < 5, so it stopped at 4 and missed 5. Changed to <= 5 to include 5.
# BUG: Cannot join string + integer with +. Used f-string to convert total to text.
print(f"Sum of 1 to 5 is: {total}")
