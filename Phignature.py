import hashlib
print("""
  ____________________________________________________________________________________________________
 /|__________________________________________| WELCOME TO |__________________________________________|
| | /$$$$$$$  /$$   /$$   /$$    /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$$ /$$   /$$ /$$$$$$$  /$$$$$$$$|
| || $$__  $$| $$  | $$ /$$$$   /$$__  $$| $$$ | $$ /$$__  $$|__  $$__/| $$  | $$| $$__  $$| $$_____/|
| || $$  \ $$| $$  | $$|_  $$  | $$  \__/| $$$$| $$| $$  \ $$   | $$   | $$  | $$| $$  \ $$| $$      |
| || $$$$$$$/| $$$$$$$$  | $$  | $$ /$$$$| $$ $$ $$| $$$$$$$$   | $$   | $$  | $$| $$$$$$$/| $$$$$   |
| || $$____/ | $$__  $$  | $$  | $$|_  $$| $$  $$$$| $$__  $$   | $$   | $$  | $$| $$__  $$| $$__/   |
| || $$      | $$  | $$  | $$  | $$  \ $$| $$\  $$$| $$  | $$   | $$   | $$  | $$| $$  \ $$| $$      |
| || $$      | $$  | $$ /$$$$$$|  $$$$$$/| $$ \  $$| $$  | $$   | $$   |  $$$$$$/| $$  | $$| $$$$$$$$|
| ||__/      |__/  |__/|______/ \______/ |__/  \__/|__/  |__/   |__/    \______/ |__/  |__/|________/|
| |                                                                                                  |
| |__________________________| THE ALL ENCOMPASING FILE SIGNATURE UTILITY |__________________________|
|/__________________________________________________________________________________________________/  
""")

def md5_sum(data):
    #returns the md5 sum from the inputed text
    return hashlib.md5(data).hexdigest()

def main():
    # Prompt the user for the data for which to generate the MD5 sum
    data_type = input('Enter "F" for file or "S" for string: ')
    if data_type == 'F' or data_type == 'f':
        filename = input('Enter the path of the file: ')
        with open(filename, 'rb') as f:
            data = f.read()
    elif data_type == 'S' or data_type == 's':
        data = input('Enter the string: ')
        data = str.encode(data)
        
    # Generate the MD5 sum of the data
    md5 = md5_sum(data)

    # Prompt the user for the name of the log file
    log_filename = input('Enter the name of the log file: ')
    log_location = input('Where eould you like the log file to be saved? ')
    log_location = log_location.replace("\\", "/")

    #adds '.txt' to the name of variable so it can be opened in a text editor
    log_filename = log_location + log_filename + '.txt'
    # Open the log file in append mode
    with open(log_filename, 'a') as log_file:
        # Write the MD5 sum to the log file
        log_file.write('MD5 sum: {}\n'.format(md5))

main()
