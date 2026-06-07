from server import hash_password, verify_password


def test_password_hashing_and_verification():
    password = "admin123"

    hashed_password = hash_password(password)

    assert hashed_password != password
    assert verify_password(password, hashed_password) is True
    assert verify_password("wrong-password", hashed_password) is False