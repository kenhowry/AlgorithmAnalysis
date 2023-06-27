"""
Algorithm Analysis:
This program implements three different algorithms that solve the same problem, 
compares their running times empirically, and analyzes them 

Each algorithm takes a sorted list of positive and negative integers with no zeroes 
and determines if there exists some value x such that both x and -x are in the list

File Name: howry_algorithm_analysis.py
Author: Ken Howry
Date: 20.4.23
Course: COMP 1353
Assignment: Project II
Collaborators: N/A
Internet Source: N/A
"""
import random
from time import time

def algorithm_1(some_list: list[int]) -> bool:
    """
        Description of Function:
            performs a sequential search to determine if there exists some value x
            such that both x and -x are in a list of integers
        Parameters:
            some_list: a list of integers
        Return:
            bool
    """
    #check if the list is empty
    if len(some_list) == 0:
        raise ValueError('The list is empty.')

    #iterate through the list using a nested for-loop
    for i in range(len(some_list) - 1):
        #store the first value in a variable
        value = some_list[i]
        for j in range(1, len(some_list)):
            #if the first value plus any value in the list is zero,
            #the value x exists
            if value + some_list[j] == 0:
                return True
    
    #if the value is not found, return False
    return False           

def algorithm_2(some_list: list[int]) -> bool:
    """
        Description of Function:
            performs a binary search to determine if there exists some value x
            such that both x and -x are in a list of integers
        Parameters:
            some_list: a list of integers
        Return:
            bool
    """
    #check if the list is empty
    if len(some_list) == 0:
        raise ValueError('The list is empty.')

    #perform a binary search on each element
    for element in some_list:
        target = element * -1
        if binary_search(some_list, target) == True:
            return True
    
    #if value x is not found, return False
    return False

def binary_search(some_list: list[int], target: int) -> bool:
    """
        Description of Function:
            a binary search algorithm:
            halves the list until the target value is found
        Parameters:
            some_list: a sorted list of integers
            target: the integer value being searched for by the algorithm
        Return:
            bool
    """
    #variable assignment
    start = 0
    end = len(some_list)

    #if the list is empty, return False
    if start > end:
        return False

    #while loop
    while start < end:
        #finding the middle value
        middle = (start + end)//2 

        #if the middle value is the target, return True
        if some_list[middle] == target:
            return True
        
        #if the target is less than the middle,
        #ignore the right of the middle
        elif target < some_list[middle]:
            end = middle - 1

        #if the target is greater than the middle,
        #ignore the left of the middle
        else:
            start = middle + 1

    #if the value is not found, return False
    return False

def algorithm_3(some_list: list[int]):
    """
        Description of Function:
            advances or retreats the indices based on sum to determine 
            if there exists some value x such that both x and -x are in the list
        Parameters:
            some_list: a list of integers
        Return:
            bool
    """
    #check if the list is empty
    if len(some_list) == 0:
        raise ValueError('The list is empty.')

    #variable assignment; first and last element in list, respectively
    i = 0
    j = len(some_list) - 1

    #while loop
    while i < j:
        #if sum is zero, value x has been found
        if some_list[i] + some_list[j] == 0:
            return True
        #if the value < 0, increment i
        elif some_list[i] + some_list[j] < 0:
            i = i + 1
        #if the value > 0, decrement j
        elif some_list[i] + some_list[j] > 0:
            j = j - 1
    
    #if value x is not found, return False
    return False

def random_sorted_list(n: int):
    """
        Description of Function:
            generates a sorted list of random integers
        Parameters:
            n: the number of random integers in the list
        Return:
            a_list: list
    """
    #create a empty list
    a_list = []

    #for loop
    for i in range(n):
        #appending a random integer
        a_list.append(random.randint(1, 500))
    
    a_list.sort()

    return a_list

#main code block
#experimentally testing runtime
print(f"n\t\telapsed_time\t\truntime")
num_trial = 1000
for n in (5000, 10000, 20000, 40000, 80000):
    some_list = random_sorted_list(n)
    start = time()
    for j in range(num_trial):
        algorithm_3(some_list)
    stop = time()
    print(f"{n}\t\t{stop - start}\t\t{(stop - start)/num_trial}")