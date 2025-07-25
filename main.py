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
        printable_bytes = [
                            "00100001", "00100010", "00100011", "00100100", "00100101", "00100110", "00100111", "00100000",
                            "00101000", "00101001", "00101010", "00101011", "00101100", "00101101", "00101110", "00101111",
                            "00110000", "00110001", "00110010", "00110011", "00110100", "00110101", "00110110", "00110111",
                            "00111000", "00111001", "00111010", "00111011", "00111100", "00111101", "00111110", "00111111",
                            "01000000", "01000001", "01000010", "01000011", "01000100", "01000101", "01000110", "01000111",
                            "01001000", "01001001", "01001010", "01001011", "01001100", "01001101", "01001110", "01001111",
                            "01010000", "01010001", "01010010", "01010011", "01010100", "01010101", "01010110", "01010111",
                            "01011000", "01011001", "01011010", "01011011", "01011100", "01011101", "01011110", "01011111",
                            "01100000", "01100001", "01100010", "01100011", "01100100", "01100101", "01100110", "01100111",
                            "01101000", "01101001", "01101010", "01101011", "01101100", "01101101", "01101110", "01101111",
                            "01110000", "01110001", "01110010", "01110011", "01110100", "01110101", "01110110", "01110111",
                            "01111000", "01111001", "01111010", "01111011", "01111100", "01111101", "01111110", "00001010"
                          ]
        bytes_meaning = {b: chr(int(b, 2)) for b in printable_bytes}
        with open("output.txt", "w") as f:
            for byte_str in binary_str.split():
                if byte_str in printable_bytes:
                    f.write(bytes_meaning[byte_str])
        with open("binary_raw_output.txt", "w") as f:
            f.write(binary_str)
        with open("binary_output.txt", "w") as f:
            for byte_str in binary_str.split():
                if byte_str in printable_bytes:
                    f.write(byte_str + " ")
        print(f"Output from {input_file} written to output.txt")
    except FileNotFoundError:
        # FILE HAS NOT BEEN FOUND
        print(f"Error: {input_file} not found.")
        sys.exit(1)
    except PermissionError:
        # FILE PERMISSIONS RESTRICT THE OS MODULE
        print(f"Error: Permission denied for {input_file}.")
        sys.exit(1)
    except IsADirectoryError:
        # `input_file` IS A DIRECTORY, NOT BINARY FILE
        print(f"Error: {input_file} is a directory, not a file.")
        sys.exit(1)
    except OSError as o:
        # OS MODULE ERROR
        print(f"Error: {input_file}: {o}")
        sys.exit(1)
    except KeyboardInterrupt:
        # HANDLE KEYBOARD INTERRUPT
        print("Process interrupted by user.")
        sys.exit(130)
    except Exception as e:
        # GENERAL EXCEPTION HANDLER
        print(f"Error: {input_file}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
