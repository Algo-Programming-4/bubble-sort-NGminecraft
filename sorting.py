def bubble(lst):
    for i in range(len(lst)-1):
        for i, v in enumerate(lst[0:-1]):
            if v > lst[i+1]:
                lst[i], lst[i+1]= lst[i+1], v
    return lst


if __name__ == "__main__":
    nums = [1, 3, 8, 19, 2, 7, -8, 27]
    a = bubble(nums)
    print(a)