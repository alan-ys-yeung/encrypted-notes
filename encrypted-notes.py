# encrypted-notes.py
# CLI program that allows you to read/write, encrypt/decrypt notes in text files.
# Created by Alan Yeung
# July 21, 2025

# Use a flag to keep main loop running until user decides to quit
keep_running = True

while (keep_running):
    print('Welcome to Encrypted Notes. What would you like to do?\n'
        '\t1. Create a new note\n'
        '\t2. Open an existing note\n'
        '\t3. Delete a note\n'
        '\t4. Exit')

    print('Select an option: ', end='')

    user_option = input()