import re

identReg = r'([_a-zA-Z][_a-zA-Z0-9]*)|(\+)|(\*)|(\()|(\))|(\-)|(\/)'





def read():
    str = raw_input()
    list = re.split(r'\s', str)
    nl = []
    for st in list:
        nl.extend(re.split(identReg, st))

    ll = []
    for i in nl:
        if i != None and i != '':
            ll.append(i)
    ll.append('#')
    return ll