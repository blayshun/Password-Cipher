""" Simple Password Cipher -- Uses lists and for loops to take a user input password, encrypt it
    and copy the output password to the user clipboard
"""

import pyperclip
from cipher import encrypt

# Program on optional loop to encrypt multiple passwords
while True:

    loop = ''
    # 'password' receives input and converts to lowercase for easy encryption
    password = input('Enter a password for strong encryption: ')
    lower_password = password.lower()

    # 'break_password' initialized as an empty list to receive appends
    break_password = []

    # 'encypted_password' receives the new password one character at a time
    encrypted_password = ''

    # individual characters in 'password' are received and appended into 'break_password' list
    for character in lower_password:
        break_password.append(character)

    # test different strings
    # print(break_password)

    # individual indices of 'break_password' are iterated over to encrypt password
    for index in range(len(break_password)):
        break_password[index] = encrypt(break_password[index])

    # takes individual list values and combines them into one string 'encrypted_password'
    for character in break_password:
        encrypted_password = encrypted_password + character

    # uses module pyperclip to copy 'encrypted_password' to user clipboard
    pyperclip.copy(encrypted_password)

    # informs user that 'encrypted password' has been copied to the user clipboard.
    print('The encrypted password has been copied to your clipboard.')
    loop = input('Would you like to enter another password to encrypt? -- (Y/N): ')
    if loop == 'Y':
        continue
    else:
        break
