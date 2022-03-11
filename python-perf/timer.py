from time import time

def timed(func):
    """
    Function decorator used to measure running time.
    """
    def wrapper(*args, **kwargs):
        start = time()
        output = func(*args, **kwargs)
        end = time()
        
        print(f"{func.__name__} took {end-start:.3f} sec to run.")
        
        return output
    return wrapper