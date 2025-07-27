# encrypted-notes.py
# CLI program that allows you to read/write, encrypt/decrypt notes in text files.
# Created by Alan Yeung
# July 21, 2025

import os

# Use a flag to keep main loop running until user decides to quit
keep_running = True

while keep_running:
    print('Welcome to Encrypted Notes. What would you like to do?\n'
        '\t1. Create a new note\n'
        '\t2. Open an existing note\n'
        '\t3. Delete a note\n'
        '\t4. Exit')

    print('Select an option: ', end='')

    user_option = input()

    match user_option:
        case '1':
            print('Creating a new note.')

            print('Enter a filename: ', end='')
            filename = input()

            print('Type your message here: ', end='')
            message = input()

            with open(filename + '.txt', 'w') as file:
                file.write(message)
        case '2':
            print('Enter the name of the file to open: ', end='')

            with open(input() + '.txt', 'r') as file:
                print(file.read())
        case '3':
            print('Enter the name of the file to delete: ', end='')

            os.remove(input() + '.txt')
        case '4':
            print('Exiting program.')
            keep_running = False
        case _:
            print('Please select a valid option.')