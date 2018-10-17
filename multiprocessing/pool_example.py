#!/usr/bin/python3
# Pool class cannot be used in the interpreter. Only available in Python3
# For each Pooled process, there is a new python process created
from multiprocessing import Pool
from time import sleep

def start_function_for_processes(n):
    sleep(.3)
    result_sent_back_to_parent = n * n
    return result_sent_back_to_parent

if __name__ == '__main__':
    with Pool(processes=5) as p:
        # map(): python built-in that says 'apply this function to every element in this iterable'
        # function = start_function_for_processes()
        # iterable: range(200)
        # chunksize (default 1): 10. Defines how large of iterable to send to each process
        # this will pass a chunk of 10 items at a time
        results = p.map(start_function_for_processes, range(200), chunksize=10)
    print(results)
