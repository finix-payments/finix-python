

def join(a, b):
    assert(a != None)
    assert(b != None)

    if a.endswith('/'):
        base = a[:-1]
    else:
        base = a

    if b.startswith('/'):
        path = b[1:]
    else:
        path = b

    return base + '/' + path
