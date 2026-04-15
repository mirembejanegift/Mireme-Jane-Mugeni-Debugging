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
#I found the bug by running the code and noticing wrong output. I then checked the loop logic and found that the list was being modified during iteration and the return statement placement was affecting the result