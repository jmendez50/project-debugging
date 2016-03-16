#Juan Marcos Mendez

def add(first, second): 
    return first + second # Just changed your plus to +

def subtract(first, second):
    return first - second # saying hey subtract the first number by the scond

def multiply(first, second):
    return first * second # Saying mulitply the first and second numbers

def divide(first, second):
    try:                        # Saying try this
        return first / second   # Trying this
    except Exception as error:  # Saying if the above dont work do this
        print('I\'m sorry, I can\'t divide by zero')  #error message if failed
