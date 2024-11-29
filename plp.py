# Predefined input and output filenames
input_filename = "input.txt"
output_filename = "output.txt"

try:
    # Read the content of the input file
    with open(input_filename, "r") as input_file:
        content = input_file.readlines()

    # Modify the content (e.g., add line numbers)
    modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]

    # Write the modified content to the output file
    with open(output_filename, "w") as output_file:
        output_file.writelines(modified_content)

    print(f"File processed successfully! Check '{output_filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to read or write to the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
