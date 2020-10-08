import hashlib

def crypto(): 
    def rotate_forward (letter, key):
        new = ord(letter) + key
        if new > ord('z'):
            new = chr(new - 26)
        elif new == ord(' ') + key:
            new = ' '
        else: new = chr(new)
        return new

    def rotate_back (letter, key):
        new = ord(letter) - key
        if new == ord(' ') - key:
            new = ' '
        elif new < ord('a'):
            new = chr(new + 26)
        else: new = chr(new)
        return new

    def encrypt(message, key):
        encrypted =''
        for character in message:
            encrypted += rotate_forward(character, key)
        return encrypted

    def decrypt(message, key):
        encrypted =''
        for character in message:
            encrypted += rotate_back(character, key)
        return encrypted

    def start_encrypt ():
        f = open ('mysecret.txt', 'w')
        message = input("Message: ")
        key = 5
        f.write(encrypt(message, key))
        f.close()

    def start_decrypt ():
        f = open ('mysecret.txt', 'r')
        message = f.read()
        key = 5
        print ('\n' + decrypt(message, key))

    crypto_menu = input('\nWould you like to encrypt (e) or decrypt (d) a message?')
    if crypto_menu == 'e':
        start_encrypt()
    else: start_decrypt()

def register():
    while True:
        username = input('\nEnter a username:')
        one = input('\nEnter a password:')
        two = input('\nRetype your password:')

        if one == two:
            break
        else:
            print('\nPasswords are not the same. Try again...\n')

    f = open ('userdata.txt', 'w')
    h = hashlib.md5(one.encode())
    f.write(username + '\n' + h.hexdigest())
    f.close()
    login()

def login():
    f = open("userdata.txt", "r")

    user =(f.readline())
    password =(f.readline())

    while True:
        loginUsername = input('\nEnter your username:')
        loginPassword = input('\nEnter your password:')
        h2 = hashlib.md5(loginPassword.encode())
        loginHash = h2.hexdigest()

        if password == loginHash and user == loginUsername + '\n':
            print('\nWelcome ' + loginUsername + '!') 
            break       
        else:
            print('Your username and/or password are incorrect.')
    crypto()

menu = input ('Do you want to register (r) as a new user or login (l) as an existing user?')
if menu == 'r':
    register()
if menu == 'l':
    login()




