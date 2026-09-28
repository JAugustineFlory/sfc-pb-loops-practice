print("-----------------------------------")
print("Galvanize Sticker Printer Service:")
print("Static Images")


# ------------------------------ Image 1 ------------------------------
print("\n")
print("Image 1: The Vertical Line")
# Use a for loop to print 4 "X" characters vertically.

# your code here
for i in range(4):
    print("X")

# ------------------------------ Image 2 ------------------------------
print("\n")
print("Image 2: The Horizontal Line")
# Use a for loop to print 4 "X" characters INLINE.

# your code here
for i in range(4):
    print("X", end=" ")

# ------------------------------ Image 3 ------------------------------
print("\n")
print("Image 3: Another Vertical Line")
# Use a counter variable and a while loop to print 4 "X" characters vertically.

# your code here
counter = 0
while counter < 4:
    print("X")
    counter+=1

# ------------------------------ Image 4 ------------------------------
print("\n")
print("Image 4: Another Horizontal Line")
# Use a counter variable and a while loop to print 4 "X" characters INLINE.

# your code here
counter = 0
while counter < 4:
    print("X", end=" ")
    counter += 1

# ------------------------------ Image 5 ------------------------------
print("\n")
print("Image 5: Row and Column Numbers")
# Follow the pseudo code below to print the following pattern:
# 1234
# 1234
# 1234
# 1234

# Use a for loop that will iterate 4 times.
# Inside the for loop, make an empty print statement.
# Use a nested for loop that will iterate 4 times.
# Inside the nested loop, print the value of the inner loop counter + 1.
for i in range(4):
    print()
    for j in range(4):
        print((j + 1), end="")

# ------------------------------ Image 6 ------------------------------ #
print("\n")
print("Image 6: A Triangle of Numbers")
# Follow the pseudo code below to print the following pattern:
# 1
# 12
# 123
# 1234

# Use a for loop that will iterate 4 times.
# Inside the for loop, make an empty print statement.
# Use a nested for loop that will iterate up to the outer loop's counter value
# + 1.
# Inside the nested loop, print the value of the inner loop counter + 1.
for i in range(4):
    print()
    for j in range(i + 1):
        print(j + 1, end="")

# ------------------------------ Image 7 ------------------------------ #
print("\n")
print("Image 7: Another Row and Column Numbers")
# Follow the pseudo code below to print the following pattern:
# 1234
# 1234
# 1234
# 1234

# Start with a counter variable.
# Use a while loop that will iterate 4 times.
# Inside the while loop, make an empty print statement.
# Use a nested while loop that will iterate 4 times.
# Inside the nested loop, print the value of the inner loop counter + 1.
# Inside the nested loop, increment your other counter.
# Inside the outer while loop, increment your counter.
counter = 0
while counter < 4:
    print()
    count2 = 0
    while count2 < 4:
        print(count2 + 1, end="")
        count2 += 1
    counter += 1

# ------------------------------ Image 8 ------------------------------ #
print("\n")
print("Image 8: Another Triangle of Numbers")
# Follow the pseudo code below to print the following pattern:
# 1
# 12
# 123
# 1234

# Start with a counter variable.
# Use a while loop that will iterate 4 times.
# Inside the while loop, make an empty print statement.
# Use a nested while loop that will iterate up to the outer loop's counter
# value + 1.
# Inside the nested loop, print the value of the inner loop counter + 1.
# Inside the nested loop, increment your other counter.
# Inside the outer while loop, increment your counter.
counter = 0
while counter < 4:
    print()
    counter2 = 0
    while counter2 < counter + 1:
        print(counter2 + 1, end="")
        counter2 += 1
    counter += 1


