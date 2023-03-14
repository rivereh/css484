from tkinter import *
from PIL import Image, ImageTk
import cv2
import statistics
import time
import pickle

root = Tk()
root.title('Video Shot Boundary Detection')
inBins = []

USE_FEATURES_TXT = True


def generateInBins(path):
    # load video and set first frame to #1000
    cap = cv2.VideoCapture(path)
    cap.set(1, 1000)

    frame = 0
    success = 1

    # loop through each from 1000 to 4999 extract features
    # into inBins
    while success and frame <= 3999:
        success, image = cap.read()

        print(f'Processing frame {frame} of 3999')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_im = Image.fromarray(image)
        pixList = list(pil_im.getdata())

        # feature bins for single image
        bins = [0]*25

        for pixel in pixList:
            r, g, b = pixel
            intensity = (0.299 * r) + (0.587 * g) + (0.114 * b)
            binNum = int(intensity // 10) - 1
            bins[binNum] += 1

        inBins.append(bins)

        frame += 1

    with open('features.txt', 'wb') as file:
        pickle.dump(inBins, file)


if USE_FEATURES_TXT:
    with open('features.txt', 'rb') as file:
        inBins = pickle.load(file)
else:
    generateInBins('20020924_juve_dk_02a.mpeg')


# create list of distances between each frame
SD = [0] * 3999

for i in range(3999):
    distance = sum(abs(val1 - val2)
                   for val1, val2 in zip(inBins[i], inBins[i + 1]))

    SD[i] = distance


# create list of shot boundaries
CSet = []
FSet = []
Fs = []
Cs = []
sets = []

# calculate mean and standard deviation
mean = sum(SD) / len(SD)
std = statistics.stdev(SD)

# calculate Tb and Ts
Tb = mean + std * 11
Ts = mean * 2

# find shot boundaries
Fs_candi = None
Tor = 2
tCount = 0

for i in range(len(SD)):
    if SD[i] >= Tb:
        cItem = []
        Cs.append(i)
        cItem.append(1000 + i + 1)
        cItem.append(1000 + i + 2)
        CSet.append(cItem)
        sets.append(cItem)

    if Ts <= SD[i] < Tb and Fs_candi is None:
        Fs_candi = i
    if Fs_candi is not None and i in Cs:
        Fs_candi = None
        tCount = 0
    elif Fs_candi is not None and SD[i] < Ts:
        tCount += 1
        if tCount == Tor:
            sum = 0
            for num in SD[Fs_candi:i-1]:
                sum += num

            if sum >= Tb:
                fItem = []
                fItem.append(Fs_candi + 1001)
                fItem.append(1000 + i - 1)
                FSet.append(fItem)
                sets.append(fItem)

            Fs_candi = None
            tCount = 0
    else:
        tCount = 0


print("\nCSet Values:")
for c in CSet:
    print(f'{c[0] - 1}, {c[1] - 1}')

print("\nFSet Values:")
for f in FSet:
    print(f'{f[0]}, {f[1]}')

# print values
print(f'\nMean: {mean}')
print(f'Stdev: {std}')
print(f'Tb: {Tb}')
print(f'Ts: {Ts}')


def playShot(index):
    cap = cv2.VideoCapture('20020924_juve_dk_02a.mpeg')

    if index == len(sets) - 1:
        cap.set(1, sets[index][0])
        count = sets[index][0]
        end = 4999
    else:
        cap.set(1, sets[index][0])
        count = sets[index][0]
        end = sets[index + 1][0] - 1

    if (cap.isOpened() == False):
        print("Error opening video file")

    while (cap.isOpened()):

        ret, frame = cap.read()
        if ret == True and count < end:
            cv2.imshow('Frame', frame)
            count += 1
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


# create user interface to display shots
cols = 5
col = 0
row = 0

for i in range(len(sets)):

    cap = cv2.VideoCapture('20020924_juve_dk_02a.mpeg')
    cap.set(1, sets[i][0])
    ret, image = cap.read()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(image)

    imSize = pil_im.size
    x = int(imSize[0]/3)
    y = int(imSize[1]/3)
    imResize = pil_im.resize((x, y), Image.Resampling.LANCZOS)
    pil_im2 = ImageTk.PhotoImage(imResize)

    myButton = Button(root, image=pil_im2,
                      command=lambda index=i: playShot(index))
    myButton.image = pil_im2

    myButton.grid(row=row, column=col)

    col += 1
    if col == cols:
        col = 0
        row += 1


root.mainloop()
