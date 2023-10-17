import sys
import logging


# Configure the logging module
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


MESSAGES_FILE_PATH = r"C:\Users\yonat\Downloads\Messages.txt"
ENCRYPTION_DICTIONARY = {'56': 'A', '45': 'J', '64': 'S', '13': 'b', '32': 'k', '91': 't', '100': '.', '57': 'B', '46': 'K', '65': 'T', '14': 'c', '33': 'l', '92': 'u', '101': ';', '58': 'C', '47': 'L', '66': 'U', '15': 'd', '34': 'm', '93': 'v', '102': '‘', '59': 'D', '48': 'M', '67': 'V', '16': 'e', '35': 'n', '94': 'w', '103': '?', '40': 'E', '49': 'N', '68': 'W', '17': 'f', '36': 'o', '95': 'x', '104': '!', '41': 'F', '60': 'O', '69': 'X', '18': 'g', '37': 'p', '96': 'y', '105': ':', '42': 'G', '61': 'P', '10': 'Y', '19': 'h', '38': 'q', '97': 'z', '43': 'H', '62': 'Q', '11': 'Z', '30': 'i', '39': 'r', '98': ' ', '44': 'I', '63': 'R', '12': 'a', '31': 'j', '90': 's', '99': ','}


def encrypt_message(message):
    # checking if the message is valid
    for char in message:
        if not (char in ENCRYPTION_DICTIONARY.values()):
            logging.error(f"Invalid message string on char '{char}'")
            exit(1)
    # Log the message before encryption
    logging.info(f"Encrypting the message: {message}")

    try:
        with open(MESSAGES_FILE_PATH, 'w') as file:
            encrypted_list = [next(key for key, value in ENCRYPTION_DICTIONARY.items() if value == char) for char in list(message)]
            file.write(','.join(encrypted_list))
            logging.info(f"Finished encrypting with the message : {','.join(encrypted_list)}")
    except FileNotFoundError:
        logging.error(f"Error: File not found at path {MESSAGES_FILE_PATH}")
    except KeyError:
        logging.error("Error: Failed to parse the message. Character not found in encryption dictionary.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")


def decrypt_message():
    try:
        with open(MESSAGES_FILE_PATH, 'r') as file:
            encrypted_msg = file.read()
            if not encrypted_msg:
                return ""
            decrypted_message = ''.join(ENCRYPTION_DICTIONARY[key] for key in encrypted_msg.split(','))
            return decrypted_message
    except FileNotFoundError:
        logging.error(f"Error: File not found at path {MESSAGES_FILE_PATH}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")


def main():
    # checking program mode and action accordingly
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
