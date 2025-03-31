''' 3. Simulate Stopwatch Program
a. Desc -> Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks
b. I/P -> Start the Stopwatch and End the Stopwatch
c. Logic -> Measure the elapsed time between start and end
d. O/P -> Print the elapsed time.
'''

import time 

def stopwatch():
    input("Press Enter to start time..")
    start_time=time.time()

    input("Pres enter to end time...")
    end_time=time.time()

    elapsed_time = end_time - start_time

    print(f"Elapsed time = {elapsed_time:.2f} seconds")

stopwatch()