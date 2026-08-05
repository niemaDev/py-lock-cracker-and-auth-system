"""
4 digit PIN brute-force simulator
"""

import time

def generate_pin(number):
    """Convert an integer (0-9999) into a zero-padded 4-digit string, just like 7 -> '0007'."""
    return f"{number:04d}"


def check_pin(attempt, secret):
    """return True if the attempted PIN matches the secret PIN and display the secret pin."""
    return attempt == secret

def brute_force_attack(secret_pin, show_attempts=True, delay=0.0):
    """
    Try every PIN from 0000 to 9999 in order until secret_pin is found.
    """
    print(f"Starting brute-force simulation on a mock lock screen...")
    print(f"Target PIN length: 4 digits | Search space: 0000-9999\n")

    attempts = 0
    start_time = time.perf_counter()

    for number in range(10000):
        attempt = generate_pin(number)
        attempts += 1

        if show_attempts:
            print(f"Attempt {attempts:>5}: trying PIN {attempt}")

        if delay > 0:
            time.sleep(delay)

        if check_pin(attempt, secret_pin):
            end_time = time.perf_counter()
            elapsed = end_time - start_time
            print(f"\nPIN cracked! The correct PIN is: {attempt}")
            print(f"Total attempts: {attempts}")
            print(f"Time taken: {elapsed:.6f} seconds")
            return attempt, attempts, elapsed

    # Should never reach here since secret_pin is always a valid 4-digit string
    end_time = time.perf_counter()
    print("PIN not found (unexpected).")
    return None, attempts, end_time - start_time


def main():
    # The "mock lock screen" secret PIN. Change this to test different values.
    secret_pin = "4271"

    # Set show_attempts=False if you only want the final result (much faster,
    # since printing 10,000 lines is the slowest part of this simulation).
    # Set delay > 0 (e.g. 0.01) to slow the loop down and watch it work in real time.
    brute_force_attack(secret_pin, show_attempts=True, delay=0.0)


if __name__ == "__main__":
    main()
