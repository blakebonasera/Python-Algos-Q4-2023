def TwoSum(arr,target):
    saw = {}
    for x in range(len(arr)):
        diff = target - arr[x]
        if diff in saw:
            print([saw[diff], x])
        else:
            saw[arr[x]] = x

TwoSum([2,5,3,7,4], 6)