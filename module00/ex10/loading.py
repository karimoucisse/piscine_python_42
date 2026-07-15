
from time import sleep, time
import math

OKBLUE = '\033[94m'
ENDC = '\033[0m'

def ft_progress(lst):
    end = list(lst)[-1] + 1
    start_time = time() 
    
    for i in lst:
        end_time = time()
        elapsed_time = float(f"{end_time - start_time:.2f}")
        index = i + 1
        p = (100 * (index)) / end
        eta = (end * elapsed_time) / index
        loader_calc = 20 * p / 100
        loader = "=" * math.floor(loader_calc) + ">"
        print(f"ETA: {eta:.2f}s [{str(math.floor(p)).rjust(3)}%][{loader.ljust(21)}] {index}/{end} | elapsed time {elapsed_time}", end='\r')
        yield i

def test():
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)
test()
