''' 
LABORATORY EXERCISE 9 
SORTING DATA STRUCTURE

Choose two of the elementary sorting algorithms that were discussed, and then create a
program that will simulate the processes of the algorithms using Python 

LabExer6A_STUDENTNO.py
'''

def selection_sort(nums):
    for i in range(6):
        minpos = i
        for j in range(i,7):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)
nums = [2, 8, 5, 3, 9, 4, 1]
selection_sort(nums)
print("\nSelection Sort: ")
print(nums)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        insertion = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > insertion:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = insertion
arr = [2, 8, 5, 3, 9, 4, 1]
insertion_sort(arr)
print("Insertion Sort: ")
print(arr)

