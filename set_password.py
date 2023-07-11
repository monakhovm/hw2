#!/usr/bin/env python3


def check_user_exists(username: str) -> bool:
    """Check if the user exists in the system."""
    pass


def check_is_root_user(username: str) -> bool:
    """
    Checking if the user running the script is a root user.
    """
    pass


def check_is_current_user(username: str) -> bool:
    """
    Checking if the user executing the script is
    the user whose password is being changed.
    """
    pass


def elevate_privileges() -> None:
    """
    Elevate the rights of the script
    to change the password in the system.
    """
    pass


def check_user_has_password(username: str) -> bool:
    """Checking if the user has a password."""
    pass


def input_password() -> str:
    """
    We ask the user to enter a password and check it for compliance
    with the requirements or generate a password automatically.
    """


def validate_password(password: str) -> bool:
    """Checking the password for compliance."""
    pass


def generate_password() -> str:
    """Password generation."""
    pass
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
