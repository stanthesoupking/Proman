def toCamelCase(x):
    output = ''.join(y for y in x.title() if y.isalnum())
    return output


def inputWithDefault(text, default=""):
    x = input(text)
    if len(x) == 0:
        x = default
    
    return x