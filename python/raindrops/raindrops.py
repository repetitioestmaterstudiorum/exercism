def convert(number):
    if not isinstance(number, int):
        raise Exception('the argument "number" must be of type "int"')

    dropDivisors = {3: 'Pling', 5: 'Plang', 7: 'Plong'}

    return ''.join(drop for divisor, drop in dropDivisors.items() 
        if number % divisor == 0) or str(number)

    # str1 = 'Pling' if (number % 3 == 0) else ''
    # str2 = 'Plang' if (number % 5 == 0) else ''
    # str3 = 'Plong' if (number % 7 == 0) else ''
    # nmb = '' if (str1 or str2 or str3) else number
    
    # return f"{str1}{str2}{str3}{nmb}"
