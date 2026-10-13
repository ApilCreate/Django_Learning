def greet_name(name):
    def format_name(name):
        return name.strip().title()


    formatted_name = format_name(name)
    return f'Welcome to class {formatted_name}'

print(greet_name('  Apil Neupane  '))


# Classwork:
# Create a nested function that takes string as a parameter 
# and use a nested function inside which filter out the lowercase values from string, 
# return only uppercase character

name = 'ajfshdDHAJHUHRQjcaijsfCHAsJHF'
def uppercase_only(string):
    def filter_lowercase(string):
        uppercase = ''
        for char in string:
            if char.islower():
                continue
            elif char.isupper():
                uppercase += char
        return uppercase
    uppercase = filter_lowercase(string)
    return f'These are the uppercase {uppercase}'

print(uppercase_only(name))