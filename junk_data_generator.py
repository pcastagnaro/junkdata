import os
import random
import argparse
import string

# USAGE
# To use only alphanumeric characters: python junk_data_generator.py -c alphanumeric
# Random bytes (default): python junk_data_generator.py -s 256 -f random.bin
# Alphanumeric data: python junk_data_generator.py -s 256 -f alphanumeric.txt -a

def generate_junk_data(size_kb, alphanumeric=False):
    """Generates junk data of the specified size in kilobytes.

    Args:
        size_kb: Size of junk data in kilobytes.
        alphanumeric: If True, generates alphanumeric data; otherwise, random bytes.
    """

    size_bytes = size_kb * 1024
    if alphanumeric:
        characters = string.ascii_letters + string.digits  # Alphanumeric characters
        junk_data = ''.join(random.choice(characters) for _ in range(size_bytes)).encode('utf-8')
    else:
        junk_data = os.urandom(size_bytes)  # Use os.urandom for cryptographically secure random bytes
    return junk_data

def write_junk_to_file(data, filename="junk_data.bin"):
    """Writes the junk data to a binary file."""
    try:
        mode = "wb" if isinstance(data, bytes) else "w" #check if data is bytes or str to choose correct mode
        with open(filename, mode) as f:
            f.write(data)
        print(f"Successfully wrote {len(data) // 1024} KB of junk data to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate junk data and write it to a file.")
    parser.add_argument("-s", "--size", type=int, default=124, help="Size of junk data in kilobytes (default: 124)")
    parser.add_argument("-f", "--filename", type=str, default="junk_data.bin", help="Output filename (default: junk_data.bin)")
    parser.add_argument("-a", "--alphanumeric", action="store_true", help="Generate alphanumeric data instead of random bytes")

    args = parser.parse_args()

    size_kb = args.size
    filename = args.filename
    alphanumeric = args.alphanumeric

    if size_kb <= 0:
        print("Error: Size must be a positive integer.")
    else:
        junk_data = generate_junk_data(size_kb, alphanumeric)
        write_junk_to_file(junk_data, filename)

    #Alternative: print the data to console (Not recommended for large data)
    #print(junk_data)