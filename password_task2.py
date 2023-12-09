from password_common import validate_pw

safe = False
while not safe:
    pw = input("Enter password: ")
    safe = validate_pw(pw)
