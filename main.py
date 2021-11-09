import os

from PIL import Image

path = "/mnt/9de57c4f-a22f-48ce-9e76-377de2802e0c/pythonProject/Image Resizer/TestImages/"
dirs = os.listdir(path)


def resize():
    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            f, e = os.path.splitext(path + item)
            imResize = im.resize((200, 200), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()
