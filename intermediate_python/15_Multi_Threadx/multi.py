from multiprocessing import Process
import os
import time


def sqare_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


processes = []

num_processes = os.cpu_count()

# create processes
for i in range(num_processes):
    p = Process(target=sqare_numbers)
    processes.append(p)

print(processes)
# Start process
for p in processes:
    p.start()

# Join
for p in processes:
    p.join()


print("End Main")
