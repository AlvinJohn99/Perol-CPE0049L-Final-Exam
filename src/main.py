from src.auth import AuthService
from src.factory import ServiceFactory


def main():
    data_stream = [78, 82, 91, 65, 40, 99, 88]

    print("Original Dataset")
    print(data_stream)

    encrypt_service = ServiceFactory.create_service("encryption")
    print("\nEncrypted:")
    print(encrypt_service.execute(data_stream))

    compress_service = ServiceFactory.create_service("compression")
    print("\nCompressed:")
    print(compress_service.execute(data_stream))

    token = AuthService.generate_token("student")
    print("\nJWT Token:")
    print(token)

    print("\nVerified Payload:")
    print(AuthService.verify_token(token))


if __name__ == "__main__":
    main()