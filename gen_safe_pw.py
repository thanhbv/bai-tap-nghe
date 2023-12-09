from random import choice, shuffle
from password_common import lowercase, uppercase, digits, symbols, validate_pw

# see document about function in password_task1.py
def gen_pw(pw_len):
    upper = choice(uppercase)
    digit = choice(digits)
    symbol = choice(symbols)
    lowers = []
    for i in range(0, pw_len - 3):
        lowers += choice(lowercase)
    pw = lowers + [upper, digit, symbol] 
    shuffle(pw)
    return ''.join(pw)

pw = gen_pw(8)
validate_pw(pw)
