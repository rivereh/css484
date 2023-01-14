# PixInfo.py
# Program to start evaluating an image in python

from PIL import Image, ImageTk
import glob, os, re

class PixInfo:
    def __init__(self, master):
        self.master = master
        self.imageList = []
        self.photoList = []
        self.xmax = 0
        self.ymax = 0
        self.colorCode = []
        self.intenCode = []

        # for sorting files numerically
        infiles = glob.glob('images/*.jpg')
        infiles = sorted(infiles, key=lambda x: int(re.findall(r'\d+', x)[0]))
        infiles = [os.path.basename(p) for p in infiles]

        for infile in infiles:
            
            # Add each image (for evaluation) into a list, 
            # and a Photo from the image (for the GUI) in a list.
            # print(infile)
            im = Image.open(f'images/{infile}')

            # Resize the image for thumbnails.
            imSize = im.size
            x = int(imSize[0]/4)
            y = int(imSize[1]/4)
            imResize = im.resize((x, y), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(imResize)

            # Find the max height and width of the set of pics.
            if x > self.xmax:
                self.xmax = x
            if y > self.ymax:
                self.ymax = y

            # Add the images to the lists.
            self.imageList.append(im)
            self.photoList.append(photo)

        # Create a list of pixel data for each image and add it
        # to a list.
        for im in self.imageList[:]:
            
            pixList = list(im.getdata())
            CcBins, InBins = self.encode(pixList)
            self.colorCode.append(CcBins)
            self.intenCode.append(InBins)

    # Bin function returns an array of bins for each 
    # image, both Intensity and Color-Code methods.
    def encode(self, pixlist):

        # 2D array initilazation for bins, initialized
        # to zero.
        InBins = [0]*25
        CcBins = [0]*64

        for pixel in pixlist:
            r, g, b = pixel
            
            # intensity calculation
            intensity = (0.299 * r) + (0.587 * g) + (0.114 * b)
            binNumI = int(intensity // 10) - 1
            InBins[binNumI] += 1

            # color code calculation
            rCC = '{0:08b}'.format(r)[:2]
            gCC = '{0:08b}'.format(g)[:2]
            bCC = '{0:08b}'.format(b)[:2]
            binNumCC = int(rCC + gCC + bCC, 2)
            CcBins[binNumCC] += 1

        # Return the list of binary digits, one digit for each
        # pixel.
        return CcBins, InBins

    # Accessor functions:
    def get_imageList(self):
        return self.imageList
    
    def get_photoList(self):
        return self.photoList
    
    def get_xmax(self):
        return self.xmax
    
    def get_ymax(self):
        return self.ymax
    
    def get_colorCode(self):
        return self.colorCode
        
    def get_intenCode(self):
        return self.intenCode