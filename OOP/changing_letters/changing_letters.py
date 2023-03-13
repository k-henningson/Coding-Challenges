# When provided with a String, capitalize all vowels

# For example:

# Input : "Hello World!"

# Output : "HEllO WOrld!"

# Note: Y is not a vowel in this kata.

def swap(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for x in str:
        if x.lower() in vowels:
            result += x.upper()
        else:
            result += x
    return result

# print (swap("HelloWorld!"), "HEllOWOrld!")