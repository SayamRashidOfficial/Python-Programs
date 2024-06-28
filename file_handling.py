def process_data_using_file_methods(input_filename, output_filename):
    try:
        with open(output_filename, "w") as output_file:
            with open(input_filename, "r") as input_file:
                output_file.write(input_file.read().strip())

        print(f"Data processed and saved to {output_filename}")
    except FileNotFoundError:
        print("Input file not found. Please check the filename and try again.")

input_file = "input_data.txt"  
output_file = "output_result.txt"  
process_data_using_file_methods(input_file, output_file)









# # Approach 2: Using file methods
# def process_data_using_file_methods(input_filename, output_filename):
#     try:
#         with open(output_filename, "w") as output_file:
#             with open(input_filename, "r") as input_file:
#                 output_file.write(input_file.read().strip())

#         print(f"Data processed and saved to {output_filename}")
#     except FileNotFoundError:
#         print("Input file not found. Please check the filename and try again.")

# # Example usage
# input_file = "input_data.txt"  # Replace with your input file name
# output_file = "output_result.txt"  # Replace with your output file name
# process_data_using_file_methods(input_file, output_file)
