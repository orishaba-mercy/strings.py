
def concatenate_args(*names):
    concatenate=[]
    for n in names:
        concatenate.extend(n)
    return''.join(concatenate)    


def concatenate_kwargs(**kwargs):
    names =''
    for n in kwargs.values():
        names+=n
    return names
