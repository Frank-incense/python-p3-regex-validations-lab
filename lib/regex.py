import re

# NOTE: There are only a few tests included, so multiple solutions will work. 
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z][a-z]+\s[A-Z][a-z]+|\w+\s\w+-\w+|\w'\w+"
name_regex = re.compile(name)

phone_number = r"[0-5]{10}|[0-5]{3}-[0-5]{3}-[0-5]{4}|\([0-5]{3}\)\s[0-5]{3}-[0-5]{4}"
phone_regex = re.compile(phone_number)

email_address = r"[a-z.]+[a-z0-9]+@\w+\.[a-z]{3}"
email_regex = re.compile(email_address)