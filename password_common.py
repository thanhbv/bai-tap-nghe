lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# Define a function to reuse code in multiple place
# To define: def <function_name>(<arguments' name>): <code to be reused>
# To use (also say "call the function"): <variable_to_store_function_value> = <function_name>(<arguments' value>)
def contain(pw, letters):
    for c in pw:
        if c in letters:
            # return <value> means: The function's value is set to <value> and exit the function
            # later, when we call this function like this: x = contain("aBc", uppercase)
            # then True will be returned here as the value of function contain and be set to variable x
            return True 
    return False

# validate and return True if password is safe
def validate_pw(pw):
    safe = True
    if len(pw) < 8:
        print('Less than 8 characters')
        safe = False
    
    if not contain(pw, lowercase):
        print('No lower case letters')
        safe = False

    if not contain(pw, uppercase):
        print('No upper case letters')
        safe = False

    if not contain(pw, digits):
        print('No digit')
        safe = False

    if not contain(pw, symbols):
        print('No symbol')
        safe = False

    if safe:
        print(pw, 'is considered a safe password.')
    else:
        print(pw, 'is not considered a safe password')
    return safe
