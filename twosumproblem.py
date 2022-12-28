#Hashing Method in 2-sum problem
def findPair(nums, target):
 
    emtyset = {}
    for i, e in enumerate(nums):
        if target - e in emtyset:
            print('Pair found', (nums[emtyset.get(target - e)], nums[i]))
            return
        emtyset[e] = i
    print('No Found')
 
if __name__ == '__main__':
 
    nums = [5, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)

