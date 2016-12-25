from PIL import Image
from PIL.ImageFile import ImageFile
import os
import sys
import logging


def process_image(image_file_path, target_file_path, prefix, delta):
    img = Image.open(image_file_path)
    assert isinstance(img, ImageFile), "Invalid image: '{}'".format(image_file_path)
    (width, height) = img.size
    pixels = img.load()
    (last_black, start, end) = (-1, -1, -1)
    for y in range(height):

        flag = True
        count = 0
        for x in range(width):
            if len('{}'.format(pixels[x, y])) > 12:
                count += 1
        if count > 30:
            flag = False

        if not flag and end == -1 and start > -1:
            end = y - 1

            crop = img.crop((0, start - prefix, width, start - prefix + 1))
            for index in range(start - delta, end + delta):
                # replace line with crop
                img.paste(crop, (0, index, width, index + 1))

        if flag:
            if y - last_black > 1:
                start = y
                end = -1
            last_black = y

    img.save(target_file_path)


def print_image_rgb(image_file_path, start=0, lines=100):
    img = Image.open(image_file_path)
    assert isinstance(img, ImageFile)
    (width, height) = img.size
    pixels = img.load()
    if height < start + lines:
        end = height
    else:
        end = start + lines
    for y in range(start, end):

        print '\nLine {}: '.format(str(y).rjust(len(str(height)))),
        for x in range(width):
            print pixels[x, y],


def list_all_image_files(base_path='.'):
    all_files = os.listdir(base_path)
    result = []
    for file_name in all_files:
        file_name = os.path.abspath(os.path.join(base_path, file_name))
        if file_name.endswith('.png') or file_name.endswith('.jpg'):
            result.append(file_name)
    return result


def get_target(image_file_path):
    if not os.path.exists('target'):
        os.mkdir('target')
    if not os.path.exists('history'):
        os.mkdir('history')
    image = Image.open(image_file_path)
    assert isinstance(image, ImageFile), ''

    if (1080, 1920) == image.size:
        crop = image.crop((330, 1072, 750, 1492))
    elif (1242, 2208) == image.size:
        crop = image.crop((366, 1162, 875, 1671))
    else:
        logging.error("Unsupported image size: {}".format(image.size))
        crop = None

    if crop is not None:
        crop.save('target/tmp.png')
        crop.close()

    (file_path, file_name) = os.path.split(image.filename)
    image.save('history/{}'.format(file_name))
    image.close()

    if os.path.exists(image_file_path):
        os.remove(image_file_path)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s:%(lineno)3d %(levelname)7s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', )

    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = '.'

    if len(sys.argv) > 2:
        prefix = int(sys.argv[2])
    else:
        prefix = 4

    if len(sys.argv) > 3:
        delta = int(sys.argv[3])
    else:
        delta = 2

    image_files = list_all_image_files(base_path)

    if len(image_files) == 0:
        image_file = None
    else:
        image_file = image_files.pop()

    if image_file is not None:
        logging.info("Origin image: '{}'.".format(image_file))
        get_target(image_file)
    else:
        logging.warn("No image has been found.")

    if os.path.exists('target/tmp.png') and os.path.isfile('target/tmp.png'):
        process_image('target/tmp.png', 'target/target.png', prefix, delta)
        logging.info("New image: '{}'.".format(os.path.abspath('target/target.png')))

    else:
        logging.warn('No image has been processed.')
