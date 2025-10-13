import os
from create_image_directory import makes_directory


def saves_image(path, img_num, img):
    if not os.path.exists(path):
        makes_directory(path)

    with open('{}/{}'.format(path,
                             img_num
                             ), 'wb') as file:
        file.write(img)
