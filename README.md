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

### In Development

* File Hash Checker
* Encode/Decode
* Subnet Calculator
* Log Analyzer

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
cd "Cybersecurity Tool
```

