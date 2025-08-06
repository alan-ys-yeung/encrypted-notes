# encrypted-notes.py
# CLI program that allows you to read/write, encrypt/decrypt notes in text files.
# Created by Alan Yeung
# July 21, 2025

from cryptography.fernet import Fernet
import base64
import hashlib
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

    password = input('Enter a password: \n>')
    message = input('Type your message here:\n> ')
    with open(filepath, 'wb') as file:
        file.write(encrypt_message(message, password))
    print('Note saved.')


def open_note():
    filename = input('Enter the note file name: ').strip()
    filepath = os.path.join(NOTES_DIR, filename + '.txt')

    try:
        with open(filepath, 'rb') as file:
            encrypted_message = file.read()
            password = input('Enter the password to decrypt:\n>')
            message = decrypt_message(encrypted_message, password)
            print(message)
    except FileNotFoundError:
        print('Error: File not found.')
    except:
        print('File corrupted or wrong password.')


def delete_note():
    filename = input('Enter the file name of the note to delete: ').strip()
    filepath = os.path.join(NOTES_DIR, filename + '.txt')

    try:
        os.remove(filepath)
    except FileNotFoundError:
        print('Error: File not found.')


# Create a fixed-size 32 byte key since AES uses a 32b key
def generate_key_from_password(password: str) -> bytes:
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())


def encrypt_message(message: str, password: str) -> bytes:
    key = generate_key_from_password(password)
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())


def decrypt_message(message: bytes, password: str) -> str:
    key = generate_key_from_password(password)
    fernet = Fernet(key)
    return fernet.decrypt(message).decode()


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