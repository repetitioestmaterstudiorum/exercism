def hello():
    return 'Hello, World!'

error_message = f"hello() doesn't print 'Hello, World!', it prints {hello()}"

# break
if not hello() == 'Hello, World!':
    raise Exception(error_message)

# just log
assert (hello() == 'Hello, World!'), error_message