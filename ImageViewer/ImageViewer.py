# ImageViewer.py
# Program to start evaluating an image in python
from tkinter import *
import math
import os
import sys
import subprocess
from PixInfo import PixInfo
import statistics
dir = os.path.dirname(__file__)


# for inspecting images on mac or pc
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(os.path.join(dir, filename))
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


class ImageViewer(Frame):

    def __init__(self, master, pixInfo, resultWin):
        Frame.__init__(self, master)
        self.master = master
        self.pixInfo = pixInfo
        self.resultWin = resultWin
        self.colorCode = pixInfo.get_colorCode()
        self.intenCode = pixInfo.get_intenCode()
        # Full-sized images.
        self.imageList = pixInfo.get_imageList()
        # Thumbnail sized images.
        self.photoList = pixInfo.get_photoList()
        # Image size for formatting.
        self.xmax = pixInfo.get_xmax()
        self.ymax = pixInfo.get_ymax()
        self.relevantImages = []
        self.selectedIndex = None
        self.normalizedWeights = []

        # Create Main frame.
        mainFrame = Frame(master)
        mainFrame.pack()

        self.rel = IntVar()

        # Create Picture chooser frame.
        listFrame = Frame(mainFrame)
        listFrame.pack(side=LEFT)

        # Create Control frame.
        controlFrame = Frame(mainFrame)
        controlFrame.pack(side=RIGHT)

        # Create Preview frame.
        previewFrame = Frame(mainFrame, width=self.xmax+45, height=self.ymax)
        previewFrame.pack_propagate(0)
        previewFrame.pack(side=RIGHT)

        # Create Results frame.
        resultsFrame = Frame(self.resultWin)
        resultsFrame.pack(side=BOTTOM)
        self.canvas = Canvas(resultsFrame)
        self.resultsScrollbar = Scrollbar(resultsFrame)
        self.resultsScrollbar.pack(side=RIGHT, fill=Y)

        # Layout Picture Listbox.
        self.listScrollbar = Scrollbar(listFrame)
        self.listScrollbar.pack(side=RIGHT, fill=Y)
        self.list = Listbox(listFrame,
                            yscrollcommand=self.listScrollbar.set,
                            selectmode=BROWSE,
                            height=10)
        for i in range(len(self.imageList)):
            self.list.insert(i, self.imageList[i].filename)
        self.list.pack(side=LEFT, fill=BOTH)
        self.list.activate(1)
        self.list.bind('<<ListboxSelect>>', self.update_preview)
        self.listScrollbar.config(command=self.list.yview)

        # Layout Controls.
        button = Button(controlFrame, text="Inspect Pic",
                        fg="red", padx=10, width=10,
                        command=lambda: self.inspect_pic(
                            self.list.get(ACTIVE)))
        button.grid(row=0, sticky=E)

        self.b1 = Button(controlFrame, text="Color-Code",
                         padx=10, width=10,
                         command=lambda: self.find_distance(method='CC'))
        self.b1.grid(row=1, sticky=E)

        b2 = Button(controlFrame, text="Intensity",
                    padx=10, width=10,
                    command=lambda: self.find_distance(method='inten'))
        b2.grid(row=2, sticky=E)

        b2 = Button(controlFrame, text="Intensity + Color-Code",
                    padx=10, width=15,
                    command=lambda: self.find_distance(method='iCC'))
        b2.grid(row=3, sticky=E)

        self.resultLbl = Checkbutton(
            controlFrame, variable=self.rel, text="Relevance", onvalue=1, offvalue=0)
        self.resultLbl.grid(row=4, sticky=W)

        # Layout Preview.
        self.selectImg = Label(previewFrame, image=self.photoList[0])
        self.selectImg.pack()

    # Event "listener" for listbox change.
    def update_preview(self, event):
        i = self.list.curselection()[0]
        self.selectedIndex = i
        self.relevantImages.clear()
        self.selectImg.configure(
            image=self.photoList[int(i)])

    # Find the Manhattan Distance of each image and return a
    # list of distances between image i and each image in the
    # directory uses the comparison method of the passed
    # binList``
    def find_distance(self, method):
        distances = {}  # index, distance
        i = self.selectedIndex

        # update weights
        if len(self.relevantImages) > 0 and not (len(self.relevantImages) == 1 and self.relevantImages[0] == i):

            if i not in self.relevantImages:
                self.relevantImages.insert(0, i)

            print(self.relevantImages)
            relevantFeatures = []
            for index in self.relevantImages:
                relevantFeatures.append(
                    pixInfo.get_normalizedFeatures()[index])
            # print(relevantFeatures)
            # print(self.relevantImages)
            updatedWeights = []

            for j in range(len(relevantFeatures[0])):
                column = [row[i] for row in relevantFeatures]
                # avg = sum(column) / len(column)
                stdev = statistics.stdev(column)
                if stdev == 0:
                    updatedWeights.append(0)
                else:
                    updatedWeights.append(1 / stdev)

            updatedWeightsSum = sum(updatedWeights)
            self.normalizedWeights = []
            for j in range(len(updatedWeights)):
                self.normalizedWeights.append(
                    updatedWeights[j] / updatedWeightsSum)

            # update weights
            # for i, index in enumerate(self.relevantImages):
            #     pixInfo.weights[index] = normalizedWeights[i]

            # self.relevantImages = []

        # get pixel count of selected image
        imageIW, imageIH = self.imageList[i].size
        imageIPixelCount = imageIW * imageIH
        print(i)
        # loop through each image and get manhattan distance
        for j, imageJ in enumerate(self.imageList):
            # skip selected image from being displayed in grid
            if self.selectedIndex == j:
                continue

            # print(self.selectedIndex, j)

            # get pixel count of image being compared
            imageJW, imageJH = imageJ.size
            imageJPixelCount = imageJW * imageJH

            if j in self.relevantImages and j != i:
                distance = sum(self.normalizedWeights[index] * abs((val1/imageIPixelCount) - (val2/imageJPixelCount))
                               for index, (val1, val2) in enumerate(zip(pixInfo.get_normalizedFeatures()[i], pixInfo.get_normalizedFeatures()[j])))
                distances[j] = distance
                continue

            if method == 'inten':
                distance = sum(abs((val1/imageIPixelCount) - (val2/imageJPixelCount))
                               for val1, val2 in zip(pixInfo.get_intenCode()[i], pixInfo.get_intenCode()[j]))

            elif method == 'CC':
                distance = sum(abs((val1/imageIPixelCount) - (val2/imageJPixelCount))
                               for val1, val2 in zip(pixInfo.get_colorCode()[i], pixInfo.get_colorCode()[j]))

            elif method == 'iCC':
                distance = sum(abs((val1/imageIPixelCount) - (val2/imageJPixelCount))
                               for val1, val2 in zip(pixInfo.get_normalizedFeatures()[i], pixInfo.get_normalizedFeatures()[j]))

            # add computed distance to distances
            distances[j] = distance

        # print(distances)

        # sort distances
        distances = {k: v for k, v in sorted(
            distances.items(), key=lambda item: item[1])}

        self.update_results(distances)

    # Update the results window with the sorted results.
    def update_results(self, sortedTup):
        cols = int(math.ceil(math.sqrt(len(sortedTup))))
        fullsize = (0, 0, (self.xmax*cols), (self.ymax*cols))

        # Initialize the canvas with dimensions equal to the
        # number of results.
        self.canvas.delete(ALL)
        self.canvas.config(
            width=self.xmax*cols,
            height=self.ymax*cols/2,
            yscrollcommand=self.resultsScrollbar.set,
            scrollregion=fullsize)
        self.canvas.pack()
        self.resultsScrollbar.config(command=self.canvas.yview)

        photoRemain = []

        # retrieve images from self.photoList using keys from sortedTup
        for key in sortedTup.keys():
            photoRemain.append(
                (self.imageList[key].filename, self.photoList[key]))

        rowPos = 0
        while photoRemain:
            photoRow = photoRemain[:cols]
            photoRemain = photoRemain[cols:]
            colPos = 0

            for (filename, img) in photoRow:

                def handler(f=filename): return self.inspect_pic(f)
                link = Button(self.canvas, image=img)
                link.image = img
                link.config(command=handler)
                link.pack(side=TOP, expand=YES)

                # create picture windows
                self.canvas.create_window(
                    colPos,
                    rowPos,
                    anchor=NW,
                    window=link,
                    width=self.xmax,
                    height=self.ymax)

                if self.rel.get():
                    # create relevant buttons
                    relevantBtn = Checkbutton(self.canvas,
                                              onvalue=1, offvalue=0, command=lambda v=filename: self.update_weight(v))
                    if (int("".join(filter(str.isdigit, filename))) - 1) in self.relevantImages:
                        relevantBtn.select()
                    relevantBtn.pack()

                    self.canvas.create_window(
                        colPos,
                        rowPos,
                        anchor=NW,
                        window=relevantBtn,
                        width=20,
                        height=20)

                colPos += self.xmax

            rowPos += self.ymax

    # Open the picture with the default operating system image
    # viewer.
    def inspect_pic(self, filename):
        open_file(filename)

    def update_weight(self, filename):
        print(filename)
        imgNum = int("".join(filter(str.isdigit, filename))) - 1
        if imgNum in self.relevantImages:
            self.relevantImages.remove(imgNum)
        else:
            self.relevantImages.append(imgNum)


# Executable section.
if __name__ == '__main__':
    root = Tk()
    root.title('Image Analysis Tool')

    resultWin = Toplevel(root)
    resultWin.title('Result Viewer')
    resultWin.protocol('WM_DELETE_WINDOW', lambda: None)

    pixInfo = PixInfo(root)

    imageViewer = ImageViewer(root, pixInfo, resultWin)

    root.mainloop()
