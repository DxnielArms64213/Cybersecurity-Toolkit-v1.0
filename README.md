# CyberSecurity ToolKit V1.0

A Python-based command-line cybersecurity toolkit built as a learning and portfolio project.

The project is designed to provide a collection of small cybersecurity utilities while developing practical Python, networking, error handling, and security-related programming skills.

> **Status:** In Development

---

## Features

### Completed

* **Password Generator**

  * Generates random passwords.
  * Supports lowercase letters, uppercase letters, numbers, and symbols.
  * Uses Python's `secrets` module for cryptographically stronger random generation.
  * Allows the user to specify password length.

* **Password Strength Checker**

  * Evaluates password characteristics.
  * Checks password length and character types.
  * Provides a strength assessment based on the checks performed.

* **Hash Generator**

  * Generates hashes from user-provided input.
  * Supports:

    * SHA-256
    * SHA-512
    * SHA-1

* **IP Information**

  * Accepts an IPv4 or IPv6 address.
  * Uses Python's `ipaddress` module to validate and process addresses.
  * Provides information about the supplied IP address.

* **TCP Port Scanner**

  * Scans a user-defined range of TCP ports.
  * Validates IP addresses before scanning.
  * Validates port ranges between 1 and 65535.
  * Detects open and refused/closed ports.
  * Handles connection timeouts.
  * Handles other socket/OS errors.
  * Properly closes sockets after each connection attempt.
  * Stores and displays open and closed port results.

* **File Hash Checker**

  * Calculates hashes for files.
  * Allows file integrity to be checked by comparing calculated hashes.
  * Uses Python hashing functionality to process file contents.

* **Encode/Decode**

  * Provides encoding and decoding functionality.
  * Allows data to be converted between encoded and decoded forms.

* **Subnet Calculator**

  * Processes IP addresses and subnet information.
  * Uses Python's `ipaddress` module for subnet calculations.
  * Provides useful network information from a supplied subnet.

### In Development

* **Log Analyzer**

---

## Technologies Used

The project is written in **Python** and currently uses modules including:

* `socket`
* `ipaddress`
* `hashlib`
* `secrets`
* `string`

Additional modules may be added as development continues.

---

## Requirements

* Python 3.x
* No external packages are currently required for the core toolkit.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd "Cybersecurity ToolKit V1"
```

Run the program:

```bash
python "#CyberSecurity ToolKit V1.py"
```

---

## Usage

When the program starts, a main menu provides access to the available tools.

Example:

```text
=================================
      CYBERSECURITY TOOLKIT
=================================

1. Password Generator
2. Password Strength Checker
3. Hash Generator
4. IP Information
5. Port Scanner
6. File Hash Checker
7. Encode/Decode
8. Subnet Calculator
9. Log Analyzer
10. Exit
```

Select the desired tool and follow the prompts provided by the program.

---

## Port Scanner

The Port Scanner is designed to provide basic TCP port discovery within a specified range.

The user provides:

1. A target IP address.
2. A starting port.
3. An ending port.

The program validates the supplied information before starting the scan.

For each port, the scanner attempts to establish a TCP connection and categorises the result.

Example:

```text
22: open
23: closed
24: closed
25: timed out

Open ports: [22]
Closed ports: [23, 24]
```

The scanner is intended for use on systems and networks where the user has permission to perform scanning.

---

## Security Considerations

This project is intended for **educational purposes and authorised security testing**.

Network scanning should only be performed against systems that you own or have explicit permission to test.

The toolkit is being developed primarily as a way to learn Python programming and fundamental cybersecurity concepts.

---

## Project Goals

The main goals of this project are to:

* Improve Python programming skills.
* Develop practical cybersecurity knowledge.
* Learn how networking concepts can be implemented in Python.
* Practice error handling and input validation.
* Build useful command-line security utilities.
* Create a portfolio project demonstrating practical development skills.

---

## Development

The toolkit is being developed incrementally.

Development has included learning and applying concepts such as:

* Variables and data types
* Loops
* Conditional statements
* Functions
* Dictionaries
* Lists
* Exception handling
* Input validation
* File handling
* Hashing
* Cryptographically secure random generation
* TCP sockets
* IP addressing
* Port scanning
* Subnetting
* File integrity verification
* Data encoding and decoding

The project will continue to evolve as additional functionality is implemented.

---

## Planned Improvements

Potential future improvements include:

* More advanced port scanning
* Service/banner detection
* More detailed password analysis
* Additional hashing algorithms
* Improved file integrity verification
* More detailed subnet calculations
* Expanded log analysis and detection capabilities
* Improved command-line output
* More comprehensive testing
* Additional security-focused utilities
* Improved documentation

---

## Testing

Formal testing and screenshots will be completed once development of the toolkit is finished.

The final testing phase will cover:

* Valid and invalid user input
* Expected and unexpected inputs
* Successful operation of each tool
* Error handling
* Edge cases
* Port scanning results
* File hashing and integrity verification
* Encoding and decoding
* Subnet calculations
* Log analysis

Screenshots demonstrating the completed functionality will also be added to the repository.

---

## Disclaimer

This project is intended for educational purposes and authorised security testing. Only use it against systems and networks you own or have explicit permission to test.
