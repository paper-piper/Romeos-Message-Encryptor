import sys
import logging
import ast


# Configure the logging module
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


encryption_data_path = r"C:\Users\yonat\Downloads\A.txt"
messages_path = r"C:\Users\yonat\Downloads\Messages.txt"


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
