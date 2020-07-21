# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        #looping through the rest of the list after the current index
        for j in range(cur_index + 1, len(arr)):
            #if the item we're currently looking at is less than the smallest one we saw earlier
            if arr[j] < arr[smallest_index]:
                #reset that shit so it makes sense again
                smallest_index = j
            # TO-DO: swap
            # Your code here

            # crazy python list magic, creates a tuple and then pulls it out into these two variables. Switching these variables is the real sorting that's going on.
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    #when you're  finally done with all your looping fun
    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    #start at the end
    current_index = len(arr)
    #loop through all that jazz except the last one
    for index in range(current_index - 1):
        #loop through everything except the last one or the first one
        for compare in range(0, current_index - index - 1):
            #find out who's bigger
            if arr[compare] > arr[compare + 1]:
                # and then put the big guy at the back.
                arr[compare], arr[compare + 1] = arr[compare + 1], arr[compare]
    # after you do that a shitload of times, you're done
    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    max = 0
    for num in arr:
        if num > max - 1:
            max = num + 1
        if num < 0:
            return 'Error, negative numbers not allowed in Count Sort'

    occurences = [0] * max
    for i, j in enumerate(occurences):
        occurences[i] = arr.count(i)

    for i in range(len(occurences)):
        if i == 0:
            occurences[i] = 1
        else:
            occurences[i] += occurences[i - 1]
    sorted_list = [None] * len(arr)

    # Run through the input list
    for (index, item) in enumerate(occurences):
        # Place the item in the sorted list
        print(occurences)
        # sorted_list[occurences[item]] = item
        sorted_list = [item - 1 for item in occurences]

    return sorted_list




