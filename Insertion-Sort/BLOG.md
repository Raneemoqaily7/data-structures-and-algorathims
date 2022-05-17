# Pull Request:

[PR](https://github.com/Raneemoqaily7/data-structures-and-algorathims/pull/17)

# Selection Sort
Selection Sort is a sorting algorithm that traverses the array multiple times as it slowly builds out the sorting sequence. The traversal keeps track of the minimum value and places it in the front of the array which should be incrementally sorted.

# Problem Domain
Write a function that take an array as input and  return sorted array 
input == > array
output ==>sorted array 

# Pseudocode
```
InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```
# Trace 
[Link](https://webwhiteboard.com/board/oSdq17jiFmUdkdyJCfafVl1yzZP43fZv/)

# WhiteBoard
![](./selectionSort.png)

### Sample array [8,4,23,42,16,15]



