from integrity_monitor import calculate_hash, check_integrity
def test_calculate_hash():
    # Test case 1: Verify hash for a known file
    test_file_path = "test_file.txt"
    with open(test_file_path, "w") as file:
        file.write("This is a test file.")
    file_hash = calculate_hash(test_file_path)
    assert len(file_hash) == 64  # SHA-256 hash length is 64 characters
def test_file_integrity():
    # Test case 2: Verify integrity check for an unchanged file
    test_file = "integrity_test.txt"
    with open(test_file, "w") as file:
        file.write("Original content.")
    original_hash = calculate_hash(test_file)
    # Create baseline
    with open("baseline.txt", "w") as file:
        file.write(original_hash)
    assert check_integrity(test_file) is True
    # Modify the file
    with open(test_file, "w") as file:
        file.write(" This is a modification.")
    assert check_integrity(test_file) is False
def test_create_baseline():
    # Test case 3: Verify baseline creation
    test_file = "baseline_test.txt"
    with open(test_file, "w") as file:
        file.write("Baseline test content.")
    from integrity_monitor import create_baseline
    create_baseline(test_file)
    with open("baseline.txt", "r") as file:
        saved_hash = file.read()
    expected_hash = calculate_hash(test_file)
    assert saved_hash == expected_hash
    