from tkinter import *
from PIL import Image, ImageTk
import cv2
import statistics
import time

root = Tk()
root.title('Video Shot Boundary Detection')
inBins = []


def generateFrames(path):

    # Path to video file
    cap = cv2.VideoCapture(path)
    cap.set(1, 1000)

    # Used as counter variable
    frame = 0

    # checks whether frames were extracted
    success = 1

    while success and frame <= 3999:

        # vidObj object calls read
        # function extract frames
        success, image = cap.read()

        print(f'Processing frame {frame} of 3999')
        # Saves the frames with frame-frame
        # cv2.imwrite(f'frames/frame{frame}.jpg', image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_im = Image.fromarray(image)
        imSize = pil_im.size
        x = int(imSize[0]/4)
        y = int(imSize[1]/4)
        imResize = pil_im.resize((x, y), Image.Resampling.LANCZOS)
        pixList = list(imResize.getdata())

        bins = [0]*25

        for pixel in pixList:
            r, g, b = pixel
            intensity = (0.299 * r) + (0.587 * g) + (0.114 * b)
            binNum = int(intensity // 10) - 1
            bins[binNum] += 1

        inBins.append(bins)

        frame += 1


generateFrames('20020924_juve_dk_02a.mpeg')

SD = [0] * 3999


for i in range(3999):
    distance = sum(abs(val1 - val2)
                   for val1, val2 in zip(inBins[i], inBins[i + 1]))

    SD[i] = distance


# print(distances)

CSet = []
FSet = []
Fs = []
Cs = []

sets = []


mean = statistics.mean(SD)
std = statistics.stdev(SD)

Tb = mean + std * 11
Ts = mean * 2

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
        # Fs.append(Fs_candi)
    if Fs_candi is not None and i in Cs:
        Fs_candi = None
        tCount = 0
    elif Fs_candi is not None and SD[i] < Ts:
        tCount += 1
        if tCount == Tor:
            # Fs.append(Fs_candi + 1)
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
    print(f'{c[0]}, {c[1]}')

print("\nFSet Values:")
for f in FSet:
    print(f'{f[0]}, {f[1]}')

print("\nAll Values:")
for s in sets:
    print(f'{s[0]}, {s[1]}')


def playShot(index):
    cap = cv2.VideoCapture('20020924_juve_dk_02a.mpeg')
    if index == 0:
        cap.set(1, 1000)
        count = 1000
        end = sets[index][0]
    elif index == len(sets):
        end = 3999
    else:
        cap.set(1, sets[index - 1][1])
        count = sets[index - 1][1]
        end = sets[index][0]
    
    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video file")

    # Read until video is completed
    while (cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True and count < end:
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            # time.sleep(0.1)
            count += 1
        # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break

    # When everything done, release
    # the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()


# playShot(FSet[1][0], FSet[1][1])

# cap = cv2.VideoCapture('20020924_juve_dk_02a.mpeg')
# cap.set(1, FSet[5][0])
# ret, image = cap.read()
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# pil_im = Image.fromarray(image)

# imSize = pil_im.size
# x = int(imSize[0]/2)
# y = int(imSize[1]/2)
# imResize = pil_im.resize((x, y), Image.ANTIALIAS)
# pil_im2 = ImageTk.PhotoImage(imResize)

# myButton = Button(root, image=pil_im2)
# myButton.pack()

# root.mainloop()

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

    # myButton.pack()

root.mainloop()
