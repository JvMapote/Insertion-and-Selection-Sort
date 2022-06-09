#Insertion sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        insertion = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > insertion:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = insertion
arr = [20, 19, 25, 29, 13, 40, 47, 32, 41, 50]
insertion_sort(arr)
print("Insertion Sort: ")
print(arr)

