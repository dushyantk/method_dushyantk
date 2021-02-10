# PYTHON 2
def flatten2(list):
    for i in list:
        try:
            for j in flatten2(i):
                yield j
              
        except TypeError:
            yield i
