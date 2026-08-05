"""
Simple Login System with Lockout Protection
=============================================
Stores credentials in-memory (a dictionary) — no database involved.
Repeatedly asks for username/password until login succeeds.
Locks the account for 1 minute after 5 consecutive failed attempts.

Concepts used: variables, dictionaries, while loop, conditionals,
string formatting, functions, the datetime module.
"""

from datetime import datetime, timedelta

# ---------------------------------------------------------------------
# "Stored" user credentials (in-memory only, no database/file involved)
# ---------------------------------------------------------------------
users = {
    "admin": "pass123",
    "student": "bdu2026",
}

MAX_ATTEMPTS = 5          # how many failed tries before locking out
LOCKOUT_DURATION = timedelta(minutes=1)


def check_credentials(username, password, user_db):
    """Return True if the username exists and the password matches it."""
    return username in user_db and user_db[username] == password


def login_system():
    failed_attempts = 0
    locked_until = None  # datetime when the lockout ends, or None if not locked

    print("=== Login System ===")

    while True:
        # --- Check if we're currently in a lockout period ---
        if locked_until is not None:
            now = datetime.now()
            if now < locked_until:
                remaining = (locked_until - now).seconds
                print(f"Account locked. Try again in {remaining} second(s).")
                continue  # skip straight back to the top of the loop and re-check
            else:
                # Lockout period has passed — reset and allow attempts again
                print("Lockout period over. You may try logging in again.\n")
                locked_until = None
                failed_attempts = 0

        # --- Prompt for credentials ---
        username = input("Username: ")
        password = input("Password: ")

        # --- Validate ---
        if check_credentials(username, password, users):
            print("\nLogin Successful!")
            break  # exits the while loop, ending the program
        else:
            failed_attempts += 1
            remaining_tries = MAX_ATTEMPTS - failed_attempts
            print(f"Incorrect username or password. Attempts left: {remaining_tries}\n")

            if failed_attempts >= MAX_ATTEMPTS:
                locked_until = datetime.now() + LOCKOUT_DURATION
                print(f"Too many failed attempts. Account locked at "
                      f"{datetime.now().strftime('%H:%M:%S')} for 1 minute.\n")


if __name__ == "__main__":
    login_system()
