import multiprocessing as mp
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
    
    p1 = mp.Process(target=make_calculator_one, args=(number_list,))
    p2 = mp.Process(target=make_calculator_two, args=(number_list,))
    p3 = mp.Process(target=make_calculator_three, args=(number_list,))

    start=time.time()
    p1.start()
    p2.start()
    p3.start()
    end=time.time()
    print("Multi: " + str(end-start))

    start=time.time()
    make_calculator_one(number_list)
    make_calculator_two(number_list)
    make_calculator_three(number_list)
    end=time.time()
    print("Regular: " + str(end-start))