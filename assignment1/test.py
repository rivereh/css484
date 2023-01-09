import glob, os

# files = glob.glob('*.py')

for infile in glob.glob('images/*.jpg'):
    file, ext = os.path.splitext(infile)
    print(file, ext)