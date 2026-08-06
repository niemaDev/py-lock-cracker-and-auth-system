import time

def generate_pin(number):
    return f"{number:04d}"

def check_pin(attempt, secret):
    return attempt == secret

def brute_force_attack(secret_pin, show_attempts=True, delay=0.0):
    print("Starting brute-force simulation on a mock lock screen")
    print("Target PIN length: 4 digits | Search space: 0000-9999\n")

    attempts = 0
    start_time = time.perf_counter()

    for number in range(10000):
        attempt = generate_pin(number)
        attempts += 1

        if show_attempts:
        
            print(f"Trying PIN {attempt}")

        if delay > 0:
            time.sleep(delay)

        if check_pin(attempt, secret_pin):
            end_time = time.perf_counter()
            elapsed = end_time - start_time
            print(f"\nPIN cracked! The correct PIN is: {attempt}")
            print(f"Total attempts: {attempts}")
            print(f"Time taken: {elapsed:.6f} seconds")
            return attempt, attempts, elapsed

    end_time = time.perf_counter()
    print("PIN not found (unexpected).")
    return None, attempts, end_time - start_time

def main():
    secret_pin = "4271"
    brute_force_attack(secret_pin, show_attempts=True, delay=0.0)

if __name__ == "__main__":
    main()
