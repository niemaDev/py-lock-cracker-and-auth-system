from datetime import datetime, timedelta
import time

users = {
    "admin": "ad0123",
    "user": "goo531",
}

try_limit = 5
block_time = timedelta(minutes=1)

def check_credentials(username, password, profile):  
    return username in profile and profile[username] == password 

def login_form():
    failed_attempts = 0
    locked_until = None

    print("Member Login")

    while True:
        if locked_until is not None:
            while True:
                now = datetime.now()
                remaining = int((locked_until - now).total_seconds())

                if remaining <= 0:
                    print("\n You can try login again\n")
                    locked_until = None
                    failed_attempts = 0
                    break

                print(f"\rAccount locked. Try again after {remaining} second.", end="")
                time.sleep(1)

            continue
        username = input("Username: ")
        password = input("Password: ")

        if check_credentials(username, password, users):  
            print("\n Welcome back!")
            break
        else:
            failed_attempts += 1
            remaining_tries = try_limit - failed_attempts
            print(f"error. Attempts left: {remaining_tries}\n")

            if failed_attempts >= try_limit:
                locked_until = datetime.now() + block_time
                print(f"Too many errors. Account locked at "
                      f"{datetime.now().strftime('%H:%M:%S')} for 1 minute.\n")

if __name__ == "__main__":
    login_form()
