def test_valid_email(validator):
    assert validator.is_valid("john@example.com") == True

def test_email_no_at(validator):
    assert validator.is_valid("johnexample.com") == False

def test_email_multiple_at(validator):
    assert validator.is_valid("johne@xam@ple.com") == False

def test_email_start_at(validator):
    assert validator.is_valid("@example.com") == False
