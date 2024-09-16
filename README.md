ATM Machine Simulator with Security Features

Project Overview
This project is an ATM Machine Simulator  which I wrote in Python that simulates common ATM functionalities, such as checking balances, depositing money, and withdrawing money. As part of its functionality, it also incorporates key security features such as user authentication and password hashing to safeguard users' credentials.

The primary goal of this project is to simulate a realistic ATM system while also demonstrating my secure programming practices, especially in the context of cybersecurity.

Features
Check Balance: Allows the user to view their current account balance.
Deposit Money: The user can deposit money into their account.
Withdraw Money: The user can withdraw funds from their account if they have sufficient balance.
User Authentication: Users must log in with a username and password to access the ATM functionalities.
Password Hashing: Passwords are stored securely using SHA-256 hashing to protect against unauthorized access and data breaches.
Error Handling: The program includes error handling for invalid inputs and incorrect credentials.

Security Measures
User Authentication: Users are required to authenticate themselves with a valid username and password before accessing the ATM's functionality.
If an incorrect username or password is provided, access is denied.

Password Hashing:
The project uses SHA-256 hashing to store passwords securely. Instead of storing raw passwords, they are hashed and stored in a format that is much harder to decrypt, which adds an extra layer of security to user data.

Hidden Password Entry:
Passwords are hidden during input to protect sensitive information from being viewed while entered.

Technologies Used
Python: The core programming language used for this project.
hashlib: A Python library used for securely hashing passwords.
getpass: Used to securely capture password input without displaying the characters.

How It Works
User Authentication: When the program starts, users are prompted to log in with a username and password.
If the username exists and the password matches the stored hash, the user gains access to the ATM features.

ATM Operations: Once authenticated, users can perform the following actions:
Check Balance: View the current balance of the account.
Deposit Money: Add money to the account. Any positive amount can be deposited.
Withdraw Money: Withdraw money from the account, as long as the balance is sufficient.
The user can perform multiple transactions until they choose to exit.

Potential Future Improvements
Multi-user Support: Currently, users are hardcoded. In the future, this project could be expanded to store users and their credentials in a database or file system.
Encryption: Add more advanced encryption techniques to further protect sensitive data.
Transaction Logging: Implement a system to log each transaction (deposits, withdrawals) for audit purposes.
Account Management: Include functionality for users to create new accounts or reset passwords.

About Me
I am currently pursuing a BSc (Hons) in Cybersecurity at the Open University. This project is part of my effort to build a strong foundation in secure coding and Python programming. I am passionate about learning and applying cybersecurity principles in real-world projects to improve my skills and prepare for a career in the field.
