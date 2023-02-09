import random
import string
import time
import itertools

def generate_password(length):
    """Generates a random password of the specified length."""
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    return password

def crack_password(password, charset):
    """Brute-force password cracking function."""
    start = time.time()
    for attempt in itertools.product(charset, repeat=len(password)):
        attempt = ''.join(attempt)
        if attempt == password:
            end = time.time()
            time_taken = end - start
            return time_taken
    return -1

# Set the desired password length
password_length = 6

# Record the start time of password generation
start = time.time()

# Generate the password
password = generate_password(password_length)

# Record the end time of password generation
end = time.time()

# Calculate the time taken to generate the password
time_taken_gen = end - start

# The character set to use for the brute-force attack
charset = string.ascii_letters + string.digits + string.punctuation

# Crack the password
time_taken_crack = crack_password(password, charset)

# Print the generated password, time taken to generate the password, and time taken to crack the password
print("Generated password: ", password)
print("Time taken to generate password: {:.2f} seconds".format(time_taken_gen))
if time_taken_crack == -1:
    print("Password not found in character set.")
else:
    print("Time taken to crack password: {:.2f} seconds".format(time_taken_crack))
