import multiprocessing as mp
import threading
import time
import math

results_a = []
results_b = []
results_c = []

def make_calculator_one(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number ** 3))


def make_calculator_two(numbers):
    for number in numbers:
        results_b.append(math.sqrt(number ** 4))

def make_calculator_three(numbers):
    for number in numbers:
        results_c.append(math.sqrt(number ** 5))
        

if __name__=='__main__':
    number_list = list(range(10000000))
    #----------MULTIPROCESSING----------
    p1 = mp.Process(target=make_calculator_one, args=(number_list,))
    p2 = mp.Process(target=make_calculator_two, args=(number_list,))
    p3 = mp.Process(target=make_calculator_three, args=(number_list,))
    start=time.time()
    p1.start()
    p2.start()
    p3.start()
    end=time.time()
    print("Multi: " + str(end-start))

    #----------THREADS AND DEAMONS----------
    t1 = threading.Thread(name="hilo_1", target= make_calculator_one, args=(number_list, ))
    t2 = threading.Thread(name="hilo_2", target= make_calculator_two, args=(number_list, ),daemon=True)
    t3 = threading.Thread(name="hilo_3", target= make_calculator_three, args=(number_list, ),daemon=True)
    start2=time.time()
    t1.start()
    t1.join()
    t2.start()
    t3.start()
    end2=time.time()
    print("Threads: " + str(end2-start2))

    #----------NOTHING SPECIAL----------
    start3=time.time()
    make_calculator_one(number_list)
    make_calculator_two(number_list)
    make_calculator_three(number_list)
    end3=time.time()
    print("Regular: " + str(end3-start3))