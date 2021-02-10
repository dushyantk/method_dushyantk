# PYTHON 3
def flatten3(list):
    for i in list:
        try:
            yield from flatten3(i)
              
        except TypeError:
            yield i
