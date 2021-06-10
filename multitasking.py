# ****************************************************************************************************
#
#       Name:          Joi Wilson
#       Course:        COSC 2110 Computer Languages: Python
#       Assignment:    ParallelizedfindSum.py & Multitasking.py
#       Due Date:      12/9/2020
#       Description:   this parallelized program should find the
#                      sum of a large 2-D list of integers.
#
# ****************************************************************************************************

import time
import random
import numpy as np


# ****************************************************************************************************

rows, columns = (6, 30000)
start = time.time()
arr_A = np.empty([rows, columns])
arr_A = [[random.randint(0, 9) for i in range(columns)] for j in range(rows)]
total = 0

for i in range(rows):
    for j in range(columns):
        total = total + arr_A[i][j]

end = time.time()

print("The total is :", total)
print("Total time after parallelized process: ", end - start)

# ****************************************************************************************************
# ****************************************************************************************************
# ****************************************************************************************************
# ****************************************************************************************************

import multiprocessing


# ****************************************************************************************************

def print_stars(num):
    for i in range(num):
        print("*", end="")


# ****************************************************************************************************

def calc_sum(number_list):
    sum = 0
    for i in number_list:
        sum = sum + i
    print("\nsum is ", sum)


# ****************************************************************************************************

def display_nums(number_list):
    print("All numbers:")

    for i in number_list:
        print(i, end=" ")


if __name__ == "__main__":
    number_list = []
    print("Enter 10 values :")

    for i in range(0, 10):
        print(i + 1, ": ", end="")
        x = int(input())
        number_list.append(x)

    p1 = multiprocessing.Process(target=print_stars,
                                 args=(10,))
    p2 = multiprocessing.Process(target=calc_sum,
                                 args=(number_list,))
    p3 = multiprocessing.Process(target=display_nums,
                                 args=(number_list,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("\nDone!")
