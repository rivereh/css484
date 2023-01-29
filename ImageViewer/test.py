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

# nums = [[] for i in range(3)]

# for index, row in enumerate(nums):
#     row.append(1)
#     row.append(2)

# print(nums)


bins = [[20, 30, 30, 20, 20, 20, 20],
        [1, 5, 4, 0, 0, 5, 5],
        [2, 2, 1, 2, 2, 1, 0],
        [4, 4, 2, 2, 2, 2, 4]]

sizes = [80, 10, 5, 10]

features = []

for binIndex in range(len(bins)):
    row = []
    for element in range(len(bins[binIndex])):
        row.append(bins[binIndex][element] / sizes[binIndex])
    features.append(row)

avgs = []
stdevs = []

normalizedFeatures = [[] for i in range(4)]

for i in range(len(features[0])):
    column = [row[i] for row in features]
    avg = sum(column) / len(column)
    avgs.append(avg)
    stdev = statistics.stdev(column)
    stdevs.append(stdev)
    for index, row in enumerate(normalizedFeatures):
        if stdev == 0:
            row.append(0)
        else:
            row.append((features[index][i] - avg) / stdev)

relevantFeatures = []
relevantFeatures.append(normalizedFeatures[0])
relevantFeatures.append(normalizedFeatures[1])

updatedWeights = []
normalizedWeights = []

for j in range(len(relevantFeatures[0])):
    column = [row[j] for row in relevantFeatures]
    stdev = statistics.stdev(column)
    if stdev == 0:
        updatedWeights.append(0)
    else:
        updatedWeights.append(1 / stdev)


updatedWeightsSum = sum(updatedWeights)
for j in range(len(updatedWeights)):
    normalizedWeights.append(updatedWeights[j] / updatedWeightsSum)

print(normalizedWeights)

# print(avgs)
# print(stdevs)
# print(normalizedFeatures)
