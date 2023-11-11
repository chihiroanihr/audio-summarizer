import sys
import os
import inspect

# Get current working file's filename
def get_source_filename():
    frame = inspect.stack()[-1]
    filename = frame.filename
    return os.path.basename(filename)

# Create new file and write output results (Import Available)
def write_result(result):
    source_filename = get_source_filename()
    result_filename = source_filename.rsplit('.', 1)[0] + "_result.txt"
    result_folder = "results"
    result_path = os.path.join(result_folder, result_filename)

    # Check if the result folder exists, create it if not
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    # Write or append the result to the file
    with open(result_path, "w") as file: # "a" if os.path.exists(result_path) else "w"
        file.write(result + "\n")
        

# Example usage:
if __name__ == "__main__":
    result = "This is the result to be written."
    write_result(result)


'''
import subprocess

# Get the source file name
source_file = __file__

# Derive the result file name from the source file name
result_file = source_file.rsplit('.', 1)[0] + "_result.txt"

# Execute your code and capture the output
result = subprocess.run(["python", source_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Example usage:
if __name__ == "__main__":    
    # Write the output to the result file
    with open("result/" + result_file, 'w') as file:
        file.write(result.stdout)

    print("Execution result written to", result_file)
'''