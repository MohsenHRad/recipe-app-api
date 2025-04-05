# found = False
# list_num = random.sample(range(0, 10), 6)
# print(f'list of numbers : {list_num}')
# target = random.choice(list_num) + random.choice(list_num)
# print(f'target : {target}')
# i = 0
# for i in range(len(list_num)):
#     for j in range(i + 1, len(list_num)):
#         num1 = list_num[i]
#         num2 = list_num[j]
#         sums = num1 + num2
#         if sums == target:
#             found = True
#             print(i)
#             print(j)
#             break
#     if found:
#         break
# if not found:
#     print('not found')

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        found = False
        list_num = nums
        # print(f"list of numbers : {list_num}")
        goal = target
        # print(f"target : {goal}")
        i = 0
        for i in range(len(list_num)):
            for j in range(i + 1, len(list_num)):
                num1 = list_num[i]
                num2 = list_num[j]
                sums = num1 + num2
                if sums == goal:
                    found = True
                    print(i)
                    print(j)
                    # return [i, j]
            if found:
                break
        if not found:
            print("not found")
            return []


nums = [2, 7, 11, 15]
target = 9

sol = Solution()
sol.twoSum(nums, target)
