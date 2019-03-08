""" Cipher algorithm for substituting characters in 'break_password'
    for 'encrypted_password' to receive
"""

# 'encrypt' function used to substitute individual characters in 'break_password'


def encrypt(password):
    if password == 'a':
        password = 'c'
    elif password == 'b':
        password = 'e'
    elif password == 'c':
        password = 'h'
    elif password == 'd':
        password = 'j'
    elif password == 'e':
        password = 'g'
    elif password == 'f':
        password = 'i'
    elif password == 'g':
        password = 'k'
    elif password == 'h':
        password = 'm'
    elif password == 'i':
        password = 'o'
    elif password == 'j':
        password = 'l'
    elif password == 'k':
        password = 'n'
    elif password == 'l':
        password = 'p'
    elif password == 'm':
        password = 'r'
    elif password == 'n':
        password = 't'
    elif password == 'o':
        password = 'q'
    elif password == 'p':
        password = 's'
    elif password == 'q':
        password = 'u'
    elif password == 'r':
        password = 'v'
    elif password == 's':
        password = 'y'
    elif password == 't':
        password = 'v'
    elif password == 'u':
        password = 'x'
    elif password == 'v':
        password = 'z'
    elif password == 'w':
        password = 'a'
    elif password == 'x':
        password = 'c'
    elif password == 'y':
        password = 'e'
    elif password == 'z':
        password = 'f'

    return password
