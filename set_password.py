#!/usr/bin/env python3

import os
import subprocess
from getpass import getpass, getuser
from random import choices
from string import ascii_lowercase, ascii_uppercase, digits, punctuation, ascii_letters


# TODO: what values ​​to use?
LEN_PWD = 8
MIN_LEN_PWD = 8
MAX_LEN_PWD = 32


def check_user_exists(username: str) -> bool:
    """Check if the user exists in the system."""
    pass


def check_is_current_user(username: str) -> bool:
    """
    Checking if the user executing the script is
    the user whose password is being changed.
    """
    pass


def input_password() -> str:
    """
    We ask the user to enter a password and check it for compliance
    with the requirements or generate a password automatically.
    """
    while True:
        password = getpass("Enter new password: ")
        if not password:
            if input("Generate a password automatically? (yes/no): ").lower() == "yes":
                password = generate_password()
            else:
                continue
        if validate_password(password):
            return password
        print("Password does not meet requirements. Try again.")


def generate_password(len: int = LEN_PWD) -> str:
    """Password generation."""
    # TODO: what visible characters can not be used in the Linux system in user passwords?
    charset = ascii_letters + digits + punctuation
    while True:
        password = "".join(choices(charset, k=len))
        if validate_password(password):
            return password


def validate_password(password: str) -> bool:
    """Checking the password for compliance."""
    if MIN_LEN_PWD < len(password) > MAX_LEN_PWD:
        return False

    return not (
        set(ascii_lowercase).isdisjoint(password)
        or set(ascii_uppercase).isdisjoint(password)
        or set(digits).isdisjoint(password)
        or set(punctuation).isdisjoint(password)
    )


def set_password(username: str, password: str) -> None:
    """Setting a user password."""
    current_user = os.getenv("USER")

    if check_is_current_user:
        command = f'echo "{username}:{password}" | sudo chpasswd'
    else:
        current_password = getpass("Input current password: ")
        command = (
            'echo -e "'
            + current_password
            + "\n"
            + password
            + "\n"
            + password
            + '" | passwd '
        )

    os.system(command)


def main() -> None:
    """
    General logic of the program. We ask for a username,
    make sure the user exists. Request a password,
    set a password for a user.
    """
    username = input("Enter username: ")

    if not check_user_exists(username):
        print("User does not exist.")
        return None

    password = input_password()
    set_password(username, password)
    print("Password set successfully.")


if __name__ == "__main__":
    main()
