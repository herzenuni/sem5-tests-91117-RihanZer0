def dictionary(keys, values):
    try:
        if type(keys) and type(values) is not list:
            raise TypeError('Input argument is not a list')
    except TypeError:
        print('Argument is not a list.')
    else:
        result = dict.fromkeys(keys, None)
        result.update(zip(keys, values))
        return result

print(dictionary([2,3,4,5,6],[22,33,44,55]))