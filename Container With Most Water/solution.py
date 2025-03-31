from typing import List

# two pointer approach
def maxArea(height: List[int]) -> int:
    res = 0
    lb = 0
    rb = len(height) -1
    while lb < rb:
        res = max(min(height[lb], height[rb])*(rb-lb), res)
        if height[lb] > height[rb]:
            rb -=1
        else:
            lb +=1
        print(res, lb, rb)
    return res




# res = maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
# print(res)
#
# res = maxArea([8, 7, 2, 1])
# print(res)
#
# res = maxArea([1,0,0,0,0,0,0,2,2])
# print(res)
#
# res = maxArea([1,2,4,3])
# print(res)

# res = maxArea(
# [1,2])
# print(res)

res = maxArea([2,3,10,5,7,8,9])
print(res)



