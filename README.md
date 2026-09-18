# CyberSecurity Toolkit V1.0

A Python-based command-line cybersecurity toolkit built as a learning and portfolio project.

The project focuses on developing practical Python programming skills while implementing common cybersecurity concepts and tools.

**Status:** V1.0 — Feature Complete

---

## Features

### 1. Password Generator

* Generates random passwords
* Supports configurable password length
* Uses uppercase and lowercase letters
* Includes numbers and symbols
* Uses Python's `secrets` module for cryptographically stronger random generation

### 2. Password Strength Checker

* Checks password characteristics
* Evaluates password length
* Checks for uppercase and lowercase characters
* Checks for numbers and symbols
* Provides feedback on password strength

### 3. Hash Generator

Supports:

* SHA-256
* SHA-512
* SHA-1

Allows users to generate hashes from input data.

### 4. IP Information

* Accepts an IP address from the user
* Uses Python's `ipaddress` module
* Provides information about the supplied IP address

### 5. TCP Port Scanner

* Scans a user-defined range of TCP ports
* Supports ports `1–65535`
* Validates IP addresses and port ranges
* Identifies open ports
* Identifies refused/closed ports
* Handles connection timeouts
* Handles network errors
* Properly closes sockets after scanning
* Displays a summary of discovered open and closed ports

**Note:** The port scanner is intended for systems and networks that you own or have explicit permission to test.

### 6. File Hash Checker

* Calculates file hashes
* Supports hash comparison
* Can be used to check whether a file has changed
* Demonstrates basic file-integrity monitoring concepts

### 7. Encode / Decode

* Encodes user-provided data
* Decodes encoded data
* Provides practice with data transformation and handling

### 8. Subnet Calculator

* Accepts IP addresses and subnet information
* Uses Python's `ipaddress` module
* Calculates subnet information

### 9. Log Analyzer

Analyzes text-based log files and identifies common security-related events.

Features include:

* Counts `INFO`, `WARNING`, and `ERROR` entries
* Counts failed login attempts
* Detects suspicious PowerShell activity
* Detects newly created administrator accounts
* Stores and displays the original log lines associated with detected events
* Alerts when 5 or more failed login attempts are detected
* Handles invalid file paths
* Handles empty log files
* Uses `with open()` for automatic file handling

The analyzer provides both a summary of event counts and the individual events that were detected.

---

## Technologies Used

* Python 3
* `socket`
* `ipaddress`
* `hashlib`
* `secrets`
* `string`
* File handling
* Exception handling
* Lists and loops
* Conditional statements
* Functions

No external Python packages are currently required.

---

## Requirements

* Python 3.x
* Windows, Linux, or macOS
* No external dependencies

---

## Installation

Clone the repository:

```bash
git clone https://github.com/DxnielArms64213/Cybersecurity-Toolkit-v1.0.git
```

Navigate into the project directory:

```bash
cd Cybersecurity-Toolkit-v1.0
```

Run the program:

```bash
python "#CyberSecurity ToolKit V1.py"
```

---

## Usage

The toolkit uses a command-line menu.

Available tools:

```text
1. Password Generator
2. Password Strength Checker
3. Hash Generator
4. IP Information
5. Port Scanner
6. File Hash Checker
7. Encode / Decode
8. Subnet Calculator
9. Log Analyzer
10. Exit
```

Users can select a tool from the main menu and follow the prompts provided by the program.

---

## Log Analyzer

The Log Analyzer accepts a text log file and analyzes each line for specific events.

Example:

```text
2026-09-18 10:15:22 INFO User admin logged in
2026-09-18 10:16:03 WARNING Failed login attempt for user admin
2026-09-18 10:17:11 ERROR Database connection failed
2026-09-18 17:01:22 WARNING Suspicious PowerShell command detected
2026-09-18 18:15:42 WARNING New administrator account created: testadmin
```

The analyzer produces a summary similar to:

```text
===== Log Analysis =====
Infos: 1
Warnings: 3
Errors: 1
Failed Logins: 1
Suspicious PowerShell Events: 1
Admin Accounts Created: 1
```

It then displays the individual detected events in separate sections.

---

## Security Considerations

This project contains functionality such as port scanning and log analysis that can be used for security testing.

The tools should only be used against systems, networks, files, and environments that you own or have explicit permission to test.

The project is primarily intended for:

* Education
* Python learning
* Cybersecurity practice
* Lab environments
* Authorised security testing

---

## Project Goals

The main goals of this project are to:

* Learn Python through practical projects
* Understand fundamental cybersecurity concepts
* Develop command-line applications
* Practice exception handling and input validation
* Work with networking concepts
* Work with files and logs
* Build tools that have practical cybersecurity applications
* Develop a portfolio project demonstrating programming and cybersecurity skills

---

## Development

This project was developed incrementally while learning Python.

Concepts practised throughout the project include:

* Variables
* Data types
* Strings
* Lists
* Loops
* Conditional statements
* Functions
* Dictionaries
* User input
* Exception handling
* File handling
* Networking
* Sockets
* Hashing
* IP addressing
* Subnetting
* Basic log analysis

The project was designed to progressively increase in complexity rather than being built from a complete solution.

---

## Testing

Formal testing and screenshots will be performed after the completion of the V1 feature set.

Testing will cover:

* Valid input
* Invalid input
* Boundary values
* Invalid IP addresses
* Invalid port ranges
* Port scanning
* File handling
* Invalid file paths
* Empty files
* Hash generation
* Hash comparison
* Log analysis
* Failed login detection
* Suspicious PowerShell detection
* Administrator account detection
* Alert thresholds
* Multiple events within the same log

Testing results and screenshots will be documented separately.

---

## Planned Improvements

Future versions may include:

* Additional cybersecurity tools
* Improved error handling
* More advanced log analysis
* Additional network reconnaissance functionality
* Service detection
* Banner grabbing
* DNS tools
* Network discovery
* Improved reporting
* Exporting results to files
* Improved command-line arguments
* More advanced security detections

---

## Disclaimer

This project is intended for educational purposes and authorised security testing.

Only use the tools against systems, networks, and files that you own or have explicit permission to test.
