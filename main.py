import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    try:
        with open(input_file, 'rb') as f:
            bytes_data = f.read()
            binary_str = ' '.join(format(byte, '08b') for byte in bytes_data)
        with open('output.txt', 'w') as f:
            f.write(binary_str)
        print(f"Output from {input_file} written to output.txt")
    except Exception as e:
        print(f"Error: {input_file}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
