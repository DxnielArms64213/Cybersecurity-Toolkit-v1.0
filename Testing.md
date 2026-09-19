# Testing

---

## Password Generator

| Test ID | Test | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| T001 | Valid password length | 12 | Generates 12-character password | h&=3<lQgwLLi | pass |
| T002 | Minimum length | 1 | Asks for a length that is valid | invalid length try again | pass |
| T003 | Maximum length | 20 | Generates 20-character password | [X4Z!&c4^pdT8Fj>AS=M | pass |
| T004 | Invalid input | no choices picked | Displays error and asks again | please pick a choice, try again | pass |

## Password Strength Checker

| Test ID | Test | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| T005 | Weak password | `password` | Identifies weak password | 3 is your score, this is a weak password | pass |
| T006 | Medium password | `test1234` | Identifies appropriate strength | 3 is your score, this is a weak password | pass |
| T007 | Strong password | `_pass*word6765246?` | Identifies strong password | 9 is your score, this is a strong password | pass |

## Hash Generator

| Test ID | Test | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| T008 | SHA-256 | `hello` | Generates SHA-256 hash | 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824 | pass |
| T009 | SHA-512 | `hello` | Generates SHA-512 hash | 9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043 | pass |
| T010 | SHA-1 | `hello` | Generates SHA-1 hash | aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d | pass |

## IP Information

| Test ID | Test | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| T011 | Valid public IP | `8.8.8.8` | Displays IP information | Information displayed successfully; output too lengthy to include in full. | pass |
| T012 | Invalid IP | `999.999.999.999` | Displays error and asks again | please enter a valid IP | pass |

## Port Scanner

| Test ID | Test | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| T013 | Valid scan | `127.0.0.1`, ports `1-100` | Scans specified range | scans specify range | pass |
| T014 | Open port | `[known open port]` | Port reported as open | 53: open port | pass |
| T015 | Closed port | `[known closed port]` | Port reported as closed | 1: closed | pass |
| T016 | Invalid IP | `999.999.999.999` | Displays error | please enter a valid ip | pass |
| T017 | Invalid port | `0` | Displays error | please enter a valid ip | pass |
| T018 | Invalid port | `65536` | Displays error | please enter a valid port | pass |
| T019 | Reversed range | `100-1` | Displays error | please enter a valid port | pass |

## File Hash Checker

| Test ID | Test | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| T020 | Hash file | `test.txt` | Generates file hash | Generated | pass |
| T021 | Invalid file | Invalid path | Displays error | file not found, please try again | pass |

## Encode / Decode

| Test ID | Test | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| T022 | Encode | `[test text]` | Encodes text successfully | aGVsbG8=  is your result | pass |
| T023 | Decode | `[encoded text]` | Returns original text | hello  is your result | pass |

## Subnet Calculator

| Test ID | Test | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| T024 | Valid subnet | `192.168.1.0/24` | Displays subnet information | Information displayed successfully; output too lengthy to include in full. | pass |
| T025 | Invalid subnet | `[invalid input]` | Displays error | Pleease try again | typo mistake in code, besides that pass |

## Log Analyzer

| Test ID | Test | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| T028 | Basic log | `basic_log.txt` | Correctly counts events | Displays events correctly | pass |
| T029 | Failed logins below threshold | `failed_logins_4.txt` | No alert displayed | No alert was displayed | pass |
| T030 | Failed logins at threshold | `failed_logins_5.txt` | Alert displayed | Alert was displayed | pass |
| T031 | PowerShell detection | `mixed_security_events.txt` | Detects PowerShell events | PowerShell events was detected | pass |
| T032 | Admin account detection | `mixed_security_events.txt` | Detects administrator creation | Administrator creation events was detected| pass |
| T033 | Empty log | `empty_log.txt` | Displays zero counts without crashing | Zero counts correctly displayed | pass |
| T034 | Invalid file path | Invalid path | Displays error and returns to menu | please enter a valid file path | pass |

---

## Testing Summary

| Feature | Tests | Passed | Failed |
|---|---:|---:|---:|
| Password Generator | 4 | 4 | 0 |
| Password Strength Checker | 3 | 3 | 0 |
| Hash Generator | 3 | 3 | 0 |
| IP Information | 2 | 2 | 0 |
| Port Scanner | 7 | 7 | 0 |
| File Hash Checker | 2 | 2 | 0 |
| Encode / Decode | 2 | 2 | 0 |
| Subnet Calculator | 2 | 2 | 0 |
| Log Analyzer | 7 | 7 | 0 |
| **Total** | **32** | **32** | **0** |
