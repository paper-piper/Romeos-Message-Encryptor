"""
Author: Yoni Reichert
Program name: Romeo and julit.py
Description: Encrypt and decrypt messages into files
Date: 26-10-2023
"""

import sys
import logging


# Configure the logging module
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Global variables
MESSAGES_FILE_PATH = r"encrypted_msg.txt"
DECRYPTION_DICTIONARY = {'56': 'A', '45': 'J', '64': 'S', '13': 'b', '32': 'k', '91': 't', '100': '.', '57': 'B', '46': 'K', '65': 'T', '14': 'c', '33': 'l', '92': 'u', '101': ';', '58': 'C', '47': 'L', '66': 'U', '15': 'd', '34': 'm', '93': 'v', '102': '‘', '59': 'D', '48': 'M', '67': 'V', '16': 'e', '35': 'n', '94': 'w', '103': '?', '40': 'E', '49': 'N', '68': 'W', '17': 'f', '36': 'o', '95': 'x', '104': '!', '41': 'F', '60': 'O', '69': 'X', '18': 'g', '37': 'p', '96': 'y', '105': ':', '42': 'G', '61': 'P', '10': 'Y', '19': 'h', '38': 'q', '97': 'z', '43': 'H', '62': 'Q', '11': 'Z', '30': 'i', '39': 'r', '98': ' ', '44': 'I', '63': 'R', '12': 'a', '31': 'j', '90': 's', '99': ','}
ENCRYPTION_DICTIONARY = {v: k for k, v in DECRYPTION_DICTIONARY.items()}


def validate_message(message):
    """
    Validates that each character in the provided message string exists in DECRYPTION_DICTIONARY.
    @:param (str): The message string to be validated.
    @:raises ValueError: If any character in the message is not present in DECRYPTION_DICTIONARY.
    @:return None
    """
    for char in message:
        if not (char in DECRYPTION_DICTIONARY.values()):
            logging.error(f"Invalid message string on char '{char}'")
            raise ValueError(f"Invalid message string on char '{char}'")


def encrypt_message(message):
    """
    Encrypts a given message string and writes the encrypted message to a file.
    - Calls validate_message to ensure message validity.
    - Writes the encrypted message to MESSAGES_FILE_PATH.
    @:param message (str): The message string to be encrypted.
    @:return None
    """
    validate_message(message)
    try:
        with open(MESSAGES_FILE_PATH, 'w') as message_file:
            encrypted_list = [ENCRYPTION_DICTIONARY[char] for char in message]
            message_file.write(','.join(encrypted_list))
            logging.info(f"Finished encrypting with the message : '{message}'")
    except FileNotFoundError:
        logging.error(f"File not found at path {MESSAGES_FILE_PATH}")
    except Exception as e:
        logging.error(f"An unknown error occurred: {str(e)}")


def decrypt_message():
    """
    Decrypts a message string from a file and returns it.
    - Reads the encrypted message from MESSAGES_FILE_PATH.
    @:param None
    @:return str: The decrypted message string.
    """
    try:
        with open(MESSAGES_FILE_PATH, 'r') as message_file:
            encrypted_msg = message_file.read()
            if not encrypted_msg:
                return ""
            decrypted_message = ''.join(DECRYPTION_DICTIONARY[key] for key in encrypted_msg.split(','))
            logging.info(f"Decrypted the message: '{decrypted_message}'")
            return decrypted_message
    except FileNotFoundError:
        logging.info(f"File not found at path {MESSAGES_FILE_PATH}, so returned empty string")
        return ""
    except Exception as e:
        logging.error(f"An unknown error occurred: {str(e)}")


def main():
    # Checking program mode and action accordingly
    if len(sys.argv) < 2:
        logging.error("User didn't enter anything into sys.argv")
    elif sys.argv[1] == "encrypt":
        encrypt_message(input("Enter your message: "))
    elif sys.argv[1] == "decrypt":
        print(decrypt_message())
    else:
        logging.error("User didn't enter either encrypt or decrypt in sys.argv")


if __name__ == "__main__":
    main()
