import csv

# Step 1: Open the file in read mode
input_file = 'students_marks.csv'
output_file = 'students_marks_with_totals.csv'

try:
    # Step 2: Read the data from the CSV file and create a list of dictionaries
    students_data = []
    with open(input_file, mode='r') as file:
        reader = csv.DictReader(file)
        
        # Assuming the file has columns: Name, Math, Science, English, History
        for row in reader:
            # Step 3: Convert marks fields to integers and calculate total & average
            marks_fields = ['Math', 'Science', 'English', 'History']
            
            
            total_marks = sum(int(row[subject]) for subject in marks_fields)
            
    
            average_marks = total_marks / len(marks_fields)
            
            # Step 4: Add 'total_marks' and 'average' fields to the row dictionary
            row['total_marks'] = total_marks
            row['average'] = round(average_marks, 2)  # rounded to 2 decimal places
            
            
            students_data.append(row)

    # Step 5: Write the updated data to a new CSV file
    with open(output_file, mode='w', newline='') as file:
        
        fieldnames = list(students_data[0].keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        
        writer.writeheader()
        
        
        writer.writerows(students_data)
    
    print(f"Updated student data with totals and averages has been written to '{output_file}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except ValueError as e:
    print(f"Error in processing data: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
