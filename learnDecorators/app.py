import time # type: ignore

def timer(fx):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fx(*args, **kwargs)
        end = time.time()
        print(f"{fx.__name__} too {end-start} time to run")
        return res
    return wrapper