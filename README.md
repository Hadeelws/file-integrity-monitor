# File I ntegrity Monitor
A Python-based cybersecurity project that detects unauthorized file modification 
using SHA-256 hashing.
## Features
- Calculate SHA-256 file hashes
- Creates a baseline hash
- Compares the current file hash with the baseline
- Detects file modifications
- Provides an alert  when file integrity is compromised
- Includes automated unit tests using pytest
## Security Concept
This project demonstrates the security concept of **Integrity**

A SHA-256 hash is generated from a file's contens and sorted as a baseline. When the file 
is checked later, a new hash is calculated and compared with the original hash.

If the hashes are different, the file has been modified.

## Technologies
- Python
- SHA-256
- hashlib
- Pytest
- Git
- GitHub

## Project Structure
```text
file-integrity-monitor/
|
|______integrity_monitor.py
|______test_integrity_monitor.py
|______sample.txt
|______README.md
|______.gitignore