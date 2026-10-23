# PIN Lock
CORRECT_PIN = "1234"
tries = 0
MAX_TRIES = 3

while tries < MAX_TRIES:
    pin = input("PIN: ")
    if pin == CORRECT_PIN:
        print("Access granted")
        break
    else:
        tries = tries + 1
        if tries < MAX_TRIES:
            print("Try again")

if tries == MAX_TRIES:
    print("Card blocked")