def get_diff_num(nums):
    count=1
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i!=j and j!=k and i!=k:
                    print(nums[i],nums[j],nums[k])
                    count+=1
    return  count

nums=[1,2,3,4]
print(get_diff_num(nums))