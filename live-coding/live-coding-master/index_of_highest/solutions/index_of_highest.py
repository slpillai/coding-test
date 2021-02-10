'''
Live Coding Assignment


arr = [-1,0,5,1,5,3,4,3]

find index of the highest value in arr

print sum of all values

print average value of arr
'''

def index_of_highest(arr):
    highest_val = arr[0]
    highest_ind = 0
    for i in range(1, len(arr)):
        if arr[i] > highest_val:
            highest_val = arr[i]
            highest_ind = i
    
    return highest_ind


print(index_of_highest([-1,0,5,1,5,3,4,3]))

def sum_of_arr(arr):
    sum = 0
    for num in arr:
        sum += num

    return sum

print(sum_of_arr([-1,0,5,1,5,3,4,3]))

def avg_of_arr(arr):
    sum = sum_of_arr(arr)
    avg = sum / len(arr)
    return avg

print(avg_of_arr([-1,0,5,1,5,3,4,3]))
