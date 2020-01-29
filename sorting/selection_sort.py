def selection_sort(S, a, b):
    # This is a quicksort that moves values in place
    if a > b:
        return 
    pivot = S[b]
    left = a
    right = b-1
    while left <= right:
        # scan until you reach equal to or greater than pivot
        while left <= right and S[left]<pivot:
            left += 1
        while left<= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right -1
          
S[left], S[b] = S[b], S[left]
# make recursive calls
selection_sort(S, a, left − 1)
selection_sort(S, left + 1, b) 
        