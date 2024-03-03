nums = [2,4,8,9,5]
nums.insert(1,3) #[2,3,4,8,9,5]
nums.remove(9) #[2,3,4,8,5]
nums.insert(0, nums.count(8)) #[1,2,3,4,8,5]
print(nums[3]) #4