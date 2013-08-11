def compose(fc):
    return lambda x:ex(fc,x)

def ex(fc,x):
    for m in fc:
        x = m(x)
    return x

