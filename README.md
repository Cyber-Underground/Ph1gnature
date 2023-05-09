## Ph1gnature

This is a Python script that generates MD5 checksums for files or strings.

### Prerequisites

- Python 3.x

### How to Use
```
1. Run the script in your preferred Python environment or execute it from the command line.
```
```
2. When prompted, enter "F" to generate the MD5 sum of a file or "S" to generate the MD5 sum of a string.
```
```
3. If you chose "F", enter the path of the file. If you chose "S", enter the string.
```
```
4. Enter the name and location of the log file where the MD5 sum will be saved. The file name will automatically be given the ".txt" extension.
```

### Code Description

The script imports the hashlib module and defines a function to generate the MD5 sum. The main function prompts the user for input and generates the MD5 sum based on the user's choice. The MD5 sum is then written to the specified log file.
