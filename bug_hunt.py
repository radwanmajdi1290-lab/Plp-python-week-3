count = 1
total = 0

# BUG: The loop needed a colon after the condition so Python could read the loop block.
# BUG: The condition needed to be <= 5, otherwise the loop stopped too early and missed 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Python cannot join a string and an integer directly, so total had to be converted to a string before printing.
print("Sum of 1 to 5 is: " + str(total))
