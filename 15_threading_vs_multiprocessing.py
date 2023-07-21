# Threading in Python runs tasks 'simultaneously' but one at a time due to GIL, while multiprocessing runs tasks truly at the same time, but uses more resources."
from multiprocessing import Process
import os
import time


def square_numbers():  # Example function that takes some memory
    for i in range(100):
        i * i
    time.sleep(0.1)


processes = []
num_processes = os.cpu_count()


# Create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

# start
for p in processes:
    p.start()

# join
for p in processes:
    p.join()

print("end main")

# Use threads instead


threads = []
num_threads = 100


# Create processes
for i in range(num_threads):
    p = Process(target=square_numbers)
    threads.append(p)

# start
for t in threads:
    t.start()

# join
for t in threads:
    t.join()

print("end main")
