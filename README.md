## File Integrity Monitor
A Python-based cybersecurity tool that monitors file integrity using SHA-256 cryptographic hashing.
## Overview
The File Integrity Monitor creates a baseline of trusted file hashes and compares the current file hash against the baseline to detect unauthorized changes.
## How It Work
1.Select files to monitor.
2.Calculate their SHA-256 hashes.
3.Store the trusted hashes in a baseline.
4.Recalculate the hashes later.
5.Compare the current hashes with the baseline.
6.Report whether the files have been modified.
## Technologies
- Python
- SHA-256
- hashlib
- JSON
- Pytest
- Git & GitHub
## Features
- Creates a file integrity baseline
- Calculate SHA-256 hashes
- Detect file modifications
- Verify file integrity
- Automated testing with pytest
## Testing
The project includes automated tests using pytest.

```text
3 passed
```