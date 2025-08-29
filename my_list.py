# 1. Create an empty list called my_list.
my_list = []
print(f"Step 1: Empty list created: {my_list}")

# 2. Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# A more concise way to do this for multiple elements: my_list.extend([10, 20, 30, 40])
print(f"Step 2: Elements appended: {my_list}")

# 3. Insert the value 15 at the second position in the list.
# List indices are 0-based, so the second position is index 1.
my_list.insert(1, 15)
print(f"Step 3: Value 15 inserted at second position: {my_list}")

# 4. Extend my_list with another list [50, 60, 70].
my_list.extend([50, 60, 70])
print(f"Step 4: List extended: {my_list}")

# 5. Remove the last element from my_list.
my_list.pop() # .pop() without an argument removes the last element
print(f"Step 5: Last element removed: {my_list}")

# 6. Sort my_list in ascending order.
my_list.sort()
print(f"Step 6: List sorted in ascending order: {my_list}")

# 7. Find and print the index of the value 30 in my_list.
try:
    index_of_30 = my_list.index(30)
    print(f"Step 7: Index of value 30: {index_of_30}")
except ValueError:
    print("Step 7: Value 30 not found in the list.")

