input_file1 = 'file1.txt'
input_file2 = 'file2.txt'

output_file = 'combined_file.txt'

try:
    with open(input_file1, 'r') as file1:
        with open(input_file2, 'r') as file2:
            with open(output_file, 'w') as output:
                for line1, line2 in zip(file1, file2):
                    combined_line = f"{line1.strip()} {line2.strip()}\n"
                    output.write(combined_line)
    
    print(f"Lines from {input_file1} and {input_file2} have been combined and saved in {output_file}.")
except FileNotFoundError:
    print("One or both input files not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
