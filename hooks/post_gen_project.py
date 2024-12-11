import os
import secrets


def generate_secret_key():
    return secrets.token_hex(16)  # 32-character hexadecimal key


def main():
    project_path = os.getcwd()  # The path where the project was generated
    env_file_path = os.path.join(project_path, ".env")

    secret_key = generate_secret_key()

    with open(env_file_path, "a") as env_file:
        env_file.write(f"\nSECRET_KEY={secret_key}\n")


if __name__ == "__main__":
    main()
