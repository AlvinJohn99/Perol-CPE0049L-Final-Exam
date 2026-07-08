from src.auth import AuthService


def test_generate_token():
    token = AuthService.generate_token("student")

    assert token is not None


def test_verify_token():
    token = AuthService.generate_token("student")

    payload = AuthService.verify_token(token)

    assert payload["username"] == "student"


def test_invalid_token():
    payload = AuthService.verify_token("invalid_token")

    assert payload is None