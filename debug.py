def clean_database(record_ids):
# Requirement: Remove all odd numbers from the list
 for record_id in record_ids[:]:
           # Loop through a copy of the list to avoid skipping items while removing
   if record_id % 2 != 0:
    record_ids.remove(record_id)
 return record_ids
# Test Case
data = [1, 3, 4, 6, 7, 9, 10]
cleaned = clean_database(data)
print(f"Final List: {cleaned}")
# EXPECTED: [4, 6, 10]
# ACTUAL: [3, 4, 6, 9, 10]


def clean_database(record_ids):
 #create a new list to store even numbers
 new_list =[]
# Requirement: Remove all odd numbers from the list
 for record_id in record_ids:
         # check if the number is even
   if record_id % 2 == 0:
        # if it's even, add it to the new list
        new_list.append(record_id)
 return new_list
# Test Case
data = [1, 3, 4, 6, 7, 9, 10]
cleaned = clean_database(data)
print(f"Final List: {cleaned}")
# EXPECTED: [4, 6, 10]
# ACTUAL: [3, 4, 6, 9, 10]


#COMMENTS FOR THE FIRST LIST
# # I ran the code and noticed that the output was not as expected.

# The odd numbers were not being removed correctly.

# I used a debugger to step through the code and observe how the list was changing.

# I realized that modifying the list while iterating over it was causing some elements to be skipped.

# I also noticed that the return statement was inside the loop, which caused the function to stop after processing only one item.

# I fixed the issue by moving the return statement outside the loop and adjusting the loop logic.

# After running the code again, the output matched the expected result.



#COMMENTS FOR THE NEW LIST

 # I ran the previous code and noticed that the output was not correct.
 
# Some odd numbers were still appearing because the list was being modified during iteration.

# Original error: Removing items from the same list while looping through it caused some elements to be skipped.

# To solve this, I decided to create a new list instead of modifying the original list.

# Create a new list to store only even numbers

# Loop through each number in the original list

# Check if the number is even
      
 # If it is even, add it to the new list
         
# After checking all numbers, return the new cleaned list

# After running the code again, the output matched the expected result.