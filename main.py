import resource
from resource import *
import psutil
import time


def general_program():
    time.sleep(3)
    # this is just a sample program from documentation
    for i in range(10 ** 8):
        _ = 1 + 1
        print(getrusage(RUSAGE_SELF))
        time.sleep(5)
        print('---------------------------')

    # we get the available memory of device using psutil
    def get_memory():
        virtual_memory = psutil.virtual_memory()
        available_memory = virtual_memory.available
        # if we just wanted to use 80% of the available memory:
        # memory_limit = int(available_memory * 0.8), and we would return this value as a limit
        return int(available_memory)

    ''''
    here were setting the limit for memory calling setrlimit(int, int)
    the parameters come from the function get_memory as the current available memory
    and 
    '''''
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (get_memory() * int(1024 / 2), hard))

def heavy_task():
    data = [0] * int(1e8)
    # will test running this function and setting try catch logic to see if limits work.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    general_program()

