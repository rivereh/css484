# import glob, os

# # files = glob.glob('*.py')

# for infile in glob.glob('images/*.jpg'):
#     file, ext = os.path.splitext(infile)
#     print(file, ext)


InBins = [0]*25
CCBins = [0]*64

r, g, b = 0, 0, 0

rCC = '{0:07b}'.format(r)[:2]
gCC = '{0:07b}'.format(g)[:2]
bCC = '{0:07b}'.format(b)[:2]
binNum = int(rCC + gCC + bCC, 2)

# print(binNum)

# intensity = (0.299 * r) + (0.587 * g) + (0.114 * b)
# binNum = max(0, int(intensity // 10) - 1)

CCBins[binNum] = 1

print (CCBins)