def format_number(value, format_spec):
    # Using the format() function to convert the number
    formatted_result = format(value, format_spec)
    return formatted_result

# Testing the function with 145 and 'o'
result = format_number(145, 'o')
print(f"The number 145 in octal format is: {result}")
