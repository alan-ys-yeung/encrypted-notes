# encrypted-notes.py
# CLI program that allows you to read/write, encrypt/decrypt notes in text files.
# Created by Alan Yeung
# July 21, 2025

import os

# Use a flag to keep main loop running until user decides to quit
keep_running = True

# Create a 'notes/' directory to store notes created by this program
NOTES_DIR = 'notes'
os.makedirs(NOTES_DIR, exist_ok=True)


def create_note():
    filename = input('Enter a filename: ').strip()
    filepath = os.path.join(NOTES_DIR, filename + '.txt')

    if os.path.exists(filepath):
        print('A note with this file name already exists.')
        return

    message = input('Type your message here:\n> ')
    with open(filepath, 'w') as file:
        file.write(message)
    print('Note saved.')


def open_note():
    filename = input('Enter the note file name: ').strip()
    filepath = os.path.join(NOTES_DIR, filename + '.txt')

    try:
        with open(filepath, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print('Error: File not found.')


def delete_note():
    filename = input('Enter the file name of the note to delete: ').strip()
    filepath = os.path.join(NOTES_DIR, filename + '.txt')

    try:
        os.remove(filepath)
    except FileNotFoundError:
        print('Error: File not found.')


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
            create_note()
        case '2':
            open_note()
        case '3':
            delete_note()
        case '4':
            print('Exiting program.')
            keep_running = False
        case _:
            print('Please select a valid option.')