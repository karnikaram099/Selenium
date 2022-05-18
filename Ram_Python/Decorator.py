# def sample(func):
#     def wrapper (*args, **kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)
#     return wrapper


a = (10, 20)
def sam(func):
    def wrapper(*args,**kwargs):
        res = func(*args, **kwargs)
        return abs(res)
    return wrapper

@sam
def add(a, b):
    return a+b

print(add(10,-20))

def demo(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, str):
            return res[::-1]
    return wrapper

@demo
def demo1(string):
    return string

print(demo1("HAi"))










