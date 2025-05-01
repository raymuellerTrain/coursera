from pathlib import Path

def find_file_in_directory(filename, directory):
    directory_path = Path(directory)
    for path in directory_path.rglob(filename):
        return str(path)
    return None

# Example usage:
directory = r"Y:\Billing_7-1-2013_Forward\837 Files from Alpha\Archive"
filename = "*52179*.*"
file_path = find_file_in_directory(filename, directory)

if file_path:
    print(f"File found at: {file_path}")
# else:
#     print("File not found")

