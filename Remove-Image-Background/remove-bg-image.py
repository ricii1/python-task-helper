import sys
from rembg import remove
from os.path import isfile

def remove_background(input_path, output_path):
    if isfile(input_path) == False:
        print(f"File {input_path} not found")
        sys.exit(1)
    with open(input_path, "rb") as input_file:
        input_data = input_file.read()

    output_data = remove(input_data)

    with open(output_path, "wb") as output_file:
        output_file.write(output_data)
    print(f"Success removing background and saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 remove-bg-image.py <path_input> <path_output>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    print(f"Removing background from {input_path} and save to {output_path}...")
    remove_background(input_path, output_path)
