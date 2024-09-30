def bubble(lst):
    for i in range(len(lst)-1):
        for i, v in enumerate(lst[0:-1]):
            if v > lst[i+1]:
                lst[i], lst[i+1]= lst[i+1], v
    return lst

def selection(lst):
    for full_index in range(len(lst)-1):
        index_smallest = full_index+1
        for index, value in enumerate(lst[full_index:]):
            if value < lst[index_smallest]:
                index_smallest = index+full_index
        lst[index_smallest], lst[full_index] = lst[full_index], lst[index_smallest]
    return lst
                
                
        

if __name__ == "__main__":
    nums = [1, 3, 8, 19, 2, 7, -8, 27]
    a = selection(nums)
    print(a)