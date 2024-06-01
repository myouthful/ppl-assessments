# File Creation and Writing
try:
    with open('my_file.txt', 'w') as file:
        file.write('Hello, World!\n')
        file.write('The answer to the ultimate question of life, the universe, and everything is 42.\n')
        file.write('Today is a beautiful day.\n')
    print('File created and initial lines written successfully.')
except Exception as e:
    print(f'An error occurred while creating or writing to the file: {e}')

# File Reading and Display
try:
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print('Content of "my_file.txt":')
        print(content)
except FileNotFoundError:
    print('The file was not found.')
except PermissionError:
    print('Permission denied while trying to read the file.')
except Exception as e:
    print(f'An error occurred while reading the file: {e}')

# File Appending
try:
    with open('my_file.txt', 'a') as file:
        file.write('Appended line 1.\n')
        file.write('Appended line 2.\n')
        file.write('Appended line 3.\n')
    print('Additional lines appended successfully.')
except FileNotFoundError:
    print('The file was not found.')
except PermissionError:
    print('Permission denied while trying to append to the file.')
except Exception as e:
    print(f'An error occurred while appending to the file: {e}')
