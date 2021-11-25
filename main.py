import os
os.system('cls')
import time
def Welcome():
    try:
        welcome = int(input("""Welcome to Cloud Chaser. How may I be of assistance.
        1. View Existing Contacts.
        2. Create A Contact.
        3. Edit A Contact.
        4. Delete A Contact\n"""))
    
    except ValueError:
        os.system('cls')
        print('Please enter a digit.\n')
        time.sleep(0.5)
        os.system('cls')
        Welcome()
Welcome()
