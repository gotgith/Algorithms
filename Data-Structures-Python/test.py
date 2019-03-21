# hash_ = {
# #             ')': '(',
# #             ']': '[',
# #             '}': '{'
# #         }
# # print(hash_[']'])
#
# print(1 % 5)

# arr = [6, 6, 7]
# print(len(arr))
# print(arr.index())

# #递归步骤测试
# def Sum(arr, l):
#      if(l == len(arr)):
#          return 0
#      return arr[l] + Sum(arr, l+1)
# arr = [6, 10]
# print(Sum(arr, 0))

# for i in range(0, 10, 2):
#     print(i)

# print(len((1,2,3)))

# words = ["gin", "zen", "gig", "msg"]
# for word in words:
#     for i in word:
#         print(ord(i))

#
# codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
#                  ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
# words = ["gin", "zen", "gig", "msg"]
# for word in words:
#     res = []
#     s = set()
#     for i in word:
#         res.append(codes[ord(i) - ord('a')])
#     res1 = str(''.join(res))
#     print(res1)
#     print(len(res1))
# # s.add(str(res))
# print(s)
# print(len(s))

# a = None
# if not a:
#     print('b')

# len(set("".join(codes[ord(s) - 97] for s in word) for word in words))
# a = [1, 2]
# a.append(3)
# print(a)

# codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
#          ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
# return len(set("".join(codes[ord(s) - 97] for s in word) for word in words))

# nums1 = [1,2,2,1,3,4]
# nums2 = [2,2,3,4]
# s  = set()
# s1 = set()
# for num in nums1:
#     s.add(num)
# print(s)
# for num in nums2:
#     s1.add(num)
# print(s1)
# a = []
# for i in s1:
#     if i in s:
#         a.append(i)
# print(a)


#
# if num in s:
#         print(s)



# a = [1,2,3,4]
# if 5 in a:
#     print(True)

# a = 'aaa'
# # b = [2]
#append方法无返回值，但是会修改原来的列表。
# # b.append(a)
# # print(b)

#leetcode 350
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# from collections import Counter
# dict1 = Counter(nums1)
# print(dict1)
# res = []
# for num in nums2:
#     if num in dict1.keys():
#         res.append(num)
#         dict1[num] -= 1
#         if dict1.get(num) == 0:
#             dict1.pop(num)
# print(res)

#leetcode 347 插入函数实现
# nums = [1,1,1,2,2,3]
# k = 2
# res = []
# from collections import Counter
# dict1 = Counter(nums)
# for i in dict1.most_common(k):
#     res.append(i[0])
# print(res)

# #桶排序
# nums = [1,1,1,2,2,3]
# k = 2
# data, res = {}, []
# for i in nums:
#     data[i] = data[i] + 1 if i in data else 1
#     bucket = [[] for i in range(len(nums)+1)]
# for key in data:
#     bucket[data[key]].append(key)
# for i in range(len(bucket)-1, -1, -1):
#     if bucket[i]:
#         res.extend(bucket[i])
#     if len(res) >= k:
#         break
# print(res[:k])

nums = [1,1,1,2,2,3]
k = 2
import heapq
data, res, pq = {}, [], []
for i in nums:
    if i in data:
        data[i] += 1
    else:
        data[i] = 1
        #data[i] = data[i] + 1 if i in data else 1
print(data)
for key in data:
    # 由于heapq默认是最小堆，
    # 代码中在堆的push时给权重加了负号，
    # 这样堆顶部对应的实际上是出现次数最多的数。
    heapq.heappush(pq, (-data[key], key))
for i in range(k):
    res.append(heapq.heappop(pq)[1])
print(res)

#
# import heapq
#
# data = [1,5,3,2,8,5]
# heapq.heapify(data)
# print(data)