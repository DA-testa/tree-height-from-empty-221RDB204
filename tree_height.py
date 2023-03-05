# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    skatits = np.zeros(n)
    height = np.zeros(n)
    for i in range(n):
        if skatits[i] == 0:
            skatits[i] = 1
            height[i] += 1
            previous = [i]
            element = parents[i]
            while True:
                if element == -1:
                    break
                if skatits[element] == 0:
                    skatits[element] = 1
                    previous.append(element)
                    for x in previous:
                        height[x] += 1
                    element = parents[element]
                else:
                    u = 1
                    for x in reversed(previous):
                        height[x] = height[element]+u
                        u += 1
                    break
    max_height = int(np.max(height))
    return max_height


def main():
    # implement input form keyboard and from files
    mode = input()
    if mode[0] == "I":
        n = int(input())
        dati = input()
        parents = np.array(dati.split(), dtype=int)
        print(compute_height(n, parents))
    elif mode[0] == "F":
        file_name = input()
        if "a" in file_name:
            return
        file_name = 'test/' + file_name + '.txt'
        with open(file_name, 'r') as f:
            n = int(f.readline())
            parents = np.array(f.readline().split(), dtype=int)
    else:
        return
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))