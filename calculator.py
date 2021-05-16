

def calculate(a,b,operator):
    if a is None or b is None:
        return None

    if   '+' in operator:
        return a + b
    elif '-' in operator:
        return a - b
    elif '*' in operator:
        return a * b
    elif '/' in operator:
        return a / b
    else:
        print("There is error in arguments")
        return None


