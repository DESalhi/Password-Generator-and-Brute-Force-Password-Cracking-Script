import string
import random
import time

def generate_password(password_length, charset):
    return ''.join(random.choice(charset) for i in range(password_length))

def brute_force_password(password, charset):
    start_time = time.time()
    password_guessed = False
    attempts = 0

    while not password_guessed:
        attempt = ''.join(random.choice(charset) for i in range(len(password)))
        attempts += 1
        if attempt == password:
            password_guessed = True
            end_time = time.time()
            time_taken = end_time - start_time
            return time_taken, attempts

def main():
    while True:
        password_length = input("Enter the length of the password to generate: ")
        try:
            password_length = int(password_length)
            if password_length <= 0:
                print("Password length must be a positive integer.")
                continue
            break
        except ValueError:
            print("Password length must be a positive integer.")

    while True:
        charset = input("Enter the characters to use for the password (e.g. abcdefghijklmnopqrstuvwxyz): ")
        if all(c in string.printable for c in charset):
            break
        else:
            print("Invalid characters in the character set. Please enter only printable ASCII characters.")

    password = generate_password(password_length, charset)
    print("Password generated:", password)

    time_taken, attempts = brute_force_password(password, charset)
    print("Password cracked in %d attempts and %.2f seconds." % (attempts, time_taken))

if __name__ == '__main__':
    main()
