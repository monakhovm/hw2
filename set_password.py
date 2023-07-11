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
    pass


def validate_password(password: str) -> bool:
    """Checking the password for compliance."""
    pass


def generate_password() -> str:
    """Password generation."""
    pass


def set_password(username: str, password: str) -> None:
    """Setting a user password."""
    pass


def main() -> None:
    """
    General logic of the program. We ask for a username,
    make sure the user exists. Request a password,
    set a password for a user.
    """
    pass


if __name__ == "__main__":
    main()
