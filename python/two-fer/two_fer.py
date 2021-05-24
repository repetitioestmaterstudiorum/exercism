def two_fer(name = 'you'):
    if not (isinstance(name, str) or name == None):
        raise Exception("Argument 'name' must be of type 'str' or 'None'")

    return f"One for {name}, one for me."
