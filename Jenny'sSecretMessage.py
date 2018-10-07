'''
Codewars: Jenny's secret message.
Write a function that returns a greeting for users.
There have to be different greeting to Johnny and to other people.
'''
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name = name)