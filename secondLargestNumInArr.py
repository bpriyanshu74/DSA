def findSecondLargest(sequenceOfNumbers):
    nums = sequenceOfNumbers
    fmax = max(nums)
    smax = -1000000
    for i in nums:
        if (i > smax and i < fmax):
            smax = max(smax,i)
    if(smax == -1000000):
        return -1
    return smax