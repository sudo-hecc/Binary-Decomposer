# Binary-Decomposer
Binary-Decomposer is a Python script that reads a binary file (such as an `.exe` file), extracts its bytes, and translates printable bytes into readable ASCII text. It also outputs the binary representation of the file.

---

## Features
- Reads any binary file and processes its bytes.
- Converts each byte to its 8-bit binary representation.
- Translates printable bytes (ASCII 33 to 127) to their character equivalents.
- Writes the readable text to `output.txt`.
- Writes the full binary representation to `binary_output.txt`

---

## Usage
Download from the [releases page](https://github.com/sudo-hecc/Binary-Decomposer/releases)
To run, use:
```sh
python3 main.py your_binary_file
```
or, if you are on Windows:
```powershell
python main.py your_binary_file
```
`your_binary_file` is the binary file you want to decompose

---

## Output
- `output.txt`: Contains the readable ASCII characters found in the input file.
- `binary_output.txt`: Contains the binary representation of every byte in the input file.

---

## Requirements
- Python 3.x

---

## Error Handling
If the input file is not provided or cannot be read, the script will print an error message and exit. **Please report to [Github Issues](https://github.com/sudo-hecc/Binary-Decomposer/issues) and refer to the [security policy](./SECURITY.md).**

---

## License
This project is licensed under the MIT license

---

### Disclaimer:
**It may not be legal to decompose certain compiled binaries. Please check licensing before doing so.**
