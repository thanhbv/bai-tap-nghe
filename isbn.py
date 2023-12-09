def isbn_weight(isbn):
    sum = 0
    weight = 1
    for x in isbn:
        sum += int(x) * weight
        # similar to:
        # if weight == 1:
        #   weight = 3
        # else:
        #   weight = 1
        weight = 3 if weight == 1 else 1
    return sum

# Task 1
isbn = input('Enter an ISBN: ')
w = isbn_weight(isbn)
print('Weighted sum: ', w)

# Task 2
if w % 10 == 0:
    print('This is a valid ISBN')
else:
    print('This is not a valid ISBN')

# Explorer task
def isbn_last_digit(s12):
    sum = isbn_weight(s12)
    # weight of 1,3,5,7,9,11,13th digit is 1
    # Note: (sum + 1*last_digit) % 10 == 0
    last_digit = 10 - sum % 10
    if last_digit == 10:
        last_digit = 0
    return str(last_digit)

s12 = input('Enter first 12 digits of an ISBN: ')
last_digit = isbn_last_digit(s12)
print('Last digit: ', last_digit)
isbn = s12 + last_digit
w = isbn_weight(isbn)
print('valid? ', w, w % 10 == 0)
