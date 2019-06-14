def toCamelCase(x):
    output = ''.join(y for y in x.title() if y.isalnum())
    return output