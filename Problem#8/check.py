def in_order(nums):
    # Type your code here.
    allCorrect = 0
    for i in range(len(nums)-1):
        if(nums[i+1] < nums[i]):
            print('Not in order')
        else:
            allCorrect += 1
    if(allCorrect == len(nums)-1):
        print('In order')
    
if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    in_order(nums1)
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    in_order(nums2)
