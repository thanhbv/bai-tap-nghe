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

insecure = True
while insecure:
    pw = input("Enter password: ")
    insecure = len(pw) < 8 or \
        not contain(pw, lowercase) or \
        not contain(pw, uppercase) or \
        not contain(pw, digits) or \
        not contain(pw, symbols)
    if insecure:
        print(pw, 'is not considered a safe password')
    else:
        print(pw, 'is considered a safe password.')
