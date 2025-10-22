import os
from create_image_directory import makes_directory


def saves_image(path_save, image_name, image_path):
    if not os.path.exists(path_save):
        makes_directory(path_save)

    with open('{}/{}'.format(path_save, image_name), 'wb') as file:
        file.write(image_path)
