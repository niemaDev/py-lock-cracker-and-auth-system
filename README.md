# py-lock-cracker-and-auth-system

This project was assigned by our mentor at the INSA Summer Camp (Cybersecurity Department) as a Python fundamentals task. It covers two small but practical programs: a simulated PIN brute-force attack and a login system with basic security protections like failed-attempt tracking and temporary lockout.

**Submitted by:** Nimet Eyayu

**ID:** CTC_3382_26

---

## Files

- `bruteforce.py` — simulates a brute-force attack on a mock 4-digit lock screen
- `login.py` — a login system with failed-attempt lockout protection

---

## 1. bruteforce.py

Simulates how a brute-force attack works against a 4-digit PIN. The program tries every combination from `0000` to `9999` in order, printing each attempt, until it finds the one that matches a secret PIN hardcoded in the script. It also counts how many attempts it took and times the whole process.

**Concepts used:** loops, conditionals, string formatting (f-strings), functions, the `time` module.

### How to run
```bash
py bruteforce.py
```

### Sample output (tail end)
```
Attempt  4270: trying PIN 4269
Attempt  4271: trying PIN 4270
Attempt  4272: trying PIN 4271

PIN cracked! The correct PIN is: 4271
Total attempts: 4272
Time taken: 0.016297 seconds
```

You can change the secret PIN at the top of `main()` in the script to try a different target.

---

## 2. login.py

A simple login system that stores usernames and passwords in a Python dictionary (no database). It keeps prompting for a username and password in a loop until the login succeeds. After 5 consecutive failed attempts, the account locks for 1 minute — the lock time is tracked using the `datetime` module, so the program checks the real elapsed time rather than just pausing execution.

**Concepts used:** dictionaries, `while` loops, conditionals, functions, the `datetime` module, f-strings.

### How to run
```bash
py login.py
```

### Sample output
```
=== Login System ===
Username: niema
Password: niema@12
Incorrect username or password. Attempts left: 4

Username: mom
Password: umi123
Incorrect username or password. Attempts left: 3

Username: mahir
Password: 123456
Incorrect username or password. Attempts left: 2

Username: hani
Password: 987654
Incorrect username or password. Attempts left: 1

Username: hanu
Password: han123
Account locked. Try again in 60 second(s).
......
Account locked. Try again in 0 second(s).
Lockout period over. You may try logging in again.

Username: 
```

If 5 attempts fail in a row, you'll instead see:
```
Too many failed attempts. Account locked at 22:14:07 for 1 minute.
Account locked. Try again in 58 second(s).
```

Test credentials are stored directly in the `users` dictionary near the top of the script (`admin` / `pass123`, `student` / `bdu2026`).

---

## Notes

Both scripts are self-contained — no external libraries are needed beyond the Python standard library (`time`, `datetime`). Tested with Python 3.10+.
