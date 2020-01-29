def bubble_sort(array):
    n = len(array)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                
    return array


"""
Best Case: O(n)
Average Case: O(n * n)
Worst Case: O(n * n)
"""

if __name__ == '__main__':
    array1 = [3,5,9,10,566,1,12]
    bubble_sort(array1)