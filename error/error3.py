try:    
    dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}

    for x in dict_.keys():

        x + 'abc'  
except TypeError:
    print('TypeError')