def has_negatives(a):

    # use cache since up to 5,000,000 elements
    # set empty arr to append to
    cache = {}
    result = []

    # cache negative numbers to compare to ints
    for i in a:
        if i < 0:
            cache[i] = i

    # if in cache and in a, append number to arr
    for i in a:
        if i > 0:
            if -i in cache:
                result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))