import csv

# Step 1: Open the file in read mode
input_file = 'students_marks.csv'
output_file = 'students_marks_updated.csv'

# Step 2: Read the data from the CSV file and create a dictionary
students_data = []
with open(input_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Step 3: Convert marks fields to integers
        marks_fields = ['Math', 'Science', 'English', 'History']
        total_marks = sum(int(row[subject]) for subject in marks_fields)
        average_marks = total_marks / len(marks_fields)
        
        # Step 4: Add 'total_marks' and 'average' fields to the row
        row['total_marks'] = total_marks
        row['average'] = average_marks
        
        # Store the updated row in students_data list
        students_data.append(row)

# Step 5: Write the updated data to a new CSV file
with open(output_file, mode='w', newline='') as file:
    # Create a CSV DictWriter with updated field names
    fieldnames = list(students_data[0].keys())
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write headers to the CSV file
    writer.writerows(students_data)  # Write the updated data

print("Updated student data has been written to:", output_file)
