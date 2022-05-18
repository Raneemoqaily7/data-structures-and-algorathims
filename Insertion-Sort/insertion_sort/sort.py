def InsertionSort(array):
    for i in range ( 1 ,len(array)):
        j =i-1
        temp =array[i]
        while j >=0 and temp <array[j]:
              array[j+1] = array[j]
              j =j-1

        array[j+1] =temp 
    return array


if __name__ == "__main__":
    array =[8,4,23,42,16,15]
    print (InsertionSort(array))
