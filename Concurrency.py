'''
Concurrency : Dealing with multiple tasks at once(but not necessarily executing at same time)

 -> think of it like single worker switching between tasks quickly.
 -> Managing multiple tasks efficiently
 -> python acheives concurrency mainly with :
        Multithreading(threading)
        Async IO (asyncio)
'''


'''
MultiThreading :

Thread - smallest unit of execution inside a process.

what's a process: 
A process is simply a program in excecution.
eg - when we open chrome, your os starts a process for chrome.

each process has:
1- its own memory space
2- Resources (CPU time, file handles)
3 - One or more treads running inside it

What is a Thread?

A thread is the smallest unit of execution inside a process.
By default, every process starts with one thread (called the main thread).
A process can create additional threads to do work in parallel.

All threads in the same process share memory.

Multithreading = running multiple threads within the same process.

In Python, threads are managed by the threading module.

Why use it?

For I/O-bound tasks (waiting on network, disk, DB).
Threads allow concurrent execution (overlapping tasks).

. I/O Bound Problems

Suppose your program needs to:

Download files from the internet
Read/write data from disk
Query a database

These operations spend most of their time waiting (for the network, disk, or database to respond).

 Without threads: The whole program is stuck waiting until the I/O finishes.
With threads: One thread can wait on I/O while another keeps working → better responsiveness
'''


import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(3)

def print_letters():
    for ch in "ABCDE":
        print(f"Letter: {ch}")
        time.sleep(1)

#create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

#start Threads
t1.start()
t2.start()

# wait for both 2 finish
t1.join()
t2.join()

print("Done!")