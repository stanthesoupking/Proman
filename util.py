def toCamelCase(x: str):
    output = ''.join(y for y in x.title() if y.isalnum())
    return output


def toSnakeCase(x: str):
    return x.lower().replace(' ', '_')


def toKebabCase(x: str):
    return x.lower().replace(' ', '-')


def inputWithDefault(text: str, default=""):
    x = input(text)
    if len(x) == 0:
        x = default

    return x
