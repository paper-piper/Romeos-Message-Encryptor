import sys
import logging
import ast


# Configure the logging module
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


encryption_data_path = r"C:\Users\yonat\Downloads\A.txt"
messages_path = r"C:\Users\yonat\Downloads\Messages.txt"

ENCRIPTION_DICIONARY = {'56': 'A', '45': 'J', '64': 'S', '13': 'b', '32': 'k', '91': 't', '100': '.', '57': 'B', '46': 'K', '65': 'T', '14': 'c', '33': 'l', '92': 'u', '101': ';', '58': 'C', '47': 'L', '66': 'U', '15': 'd', '34': 'm', '93': 'v', '102': '‘', '59': 'D', '48': 'M', '67': 'V', '16': 'e', '35': 'n', '94': 'w', '103': '?', '40': 'E', '49': 'N', '68': 'W', '17': 'f', '36': 'o', '95': 'x', '104': '!', '41': 'F', '60': 'O', '69': 'X', '18': 'g', '37': 'p', '96': 'y', '105': ':', '42': 'G', '61': 'P', '10': 'Y', '19': 'h', '38': 'q', '97': 'z', '43': 'H', '62': 'Q', '11': 'Z', '30': 'i', '39': 'r', '98': ' ', '44': 'I', '63': 'R', '12': 'a', '31': 'j', '90': 's', '99': ','}


def encrypt_message(message):
    encryption_dictionary = get_encryption_dictionary(encryption_data_path)

    # Log the message before encryption
    logging.info(f"Encrypting the message: {message}")

    try:
        with open(messages_path, 'w') as file:
            encrypted_list = [next(key for key, value in encryption_dictionary.items() if value == char) for char in list(message)]
            file.write(','.join(encrypted_list))
            logging.info(f"Finished encrypting with the message : {','.join(encrypted_list)}")
    except FileNotFoundError:
        logging.error(f"Error: File not found at path {messages_path}")
    except KeyError:
        logging.error("Error: Failed to parse the message. Character not found in encryption dictionary.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")


def decrypt_message():
    encryption_dictionary = get_encryption_dictionary(encryption_data_path)

    try:
        with open(messages_path, 'r') as file:
            encrypted_msg = file.read()
            if not encrypted_msg:
                return ""
            decrypted_message = ''.join(encryption_dictionary[key] for key in encrypted_msg.split(','))
            return decrypted_message
    except FileNotFoundError:
        logging.error(f"Error: File not found at path {messages_path}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")


def get_encryption_dictionary(path):
    with open(path, 'r') as file:
        content = file.read()
        encryption_dictionary = ast.literal_eval(content)
        logging.info(f"the encryption dictionary: {encryption_dictionary}")
        return encryption_dictionary


def main():

    if sys.argv[1] == "encrypt":
        encrypt_message(input("Enter your message: "))
    elif sys.argv[1] == "decrypt":
        print(decrypt_message())
    else:
        print("Make sure to include decrypt or encrypt in the sys.argv")


if __name__ == "__main__":
    main()
