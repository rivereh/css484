import math
import statistics
import numpy as np
# import glob, os

# # files = glob.glob('*.py')

# for infile in glob.glob('images/*.jpg'):
#     file, ext = os.path.splitext(infile)
#     print(file, ext)


# InBins = [0]*25
# CCBins = [0]*64

# r, g, b = 0, 0, 0

# rCC = '{0:07b}'.format(r)[:2]
# gCC = '{0:07b}'.format(g)[:2]
# bCC = '{0:07b}'.format(b)[:2]
# binNum = int(rCC + gCC + bCC, 2)

# # print(binNum)

# # intensity = (0.299 * r) + (0.587 * g) + (0.114 * b)
# # binNum = max(0, int(intensity // 10) - 1)

# CCBins[binNum] = 1

# print (CCBins)

# print('{0:08b}'.format(6))

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]


# def column(matrix, i):
#     return [row[i] for row in matrix]


# # print(column(matrix, 1))


# for i in range(len(matrix)):
#     print([row[i] for row in matrix])


# nums = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]
# nums = np.array(nums)
# avg = sum(nums) / len(nums)

# stdev = math.sqrt((sum(pow(x - avg, 2) for x in nums) / 99))
# stdev = statistics.stdev(nums)

# print(array(nums[:, 2]))

nums = [[] for i in range(3)]

for index, row in enumerate(nums):
    row.append(1)
    row.append(2)

print(nums)
