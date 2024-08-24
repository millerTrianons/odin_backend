import re

email_regex_raw_str = \
    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
email_regex = re.compile(email_regex_raw_str)


def email_is_valid(email: str) -> bool:
    return bool(email_regex.fullmatch(email))


