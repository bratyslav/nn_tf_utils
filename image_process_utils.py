import matplotlib.pyplot as plt
import random
# import numpy
import cv2


def show_samples(samples_list):
    if not isinstance(samples_list, list):
        print('show_samples() argument error: {} is not a valid argument'.format(type(samples_list)))
        return
    plt.rcParams['figure.figsize'] = [6 * len(samples_list), 8]
    fig, axs = plt.subplots(1, len(samples_list))
    if len(samples_list) == 1:
        axs.imshow(samples_list[0])
    else:
        for i, img in enumerate(samples_list):
            axs[i].imshow(img)
    plt.show()


def random_crop_resize(img_list, output_h, output_w, max_downscale=0.5, get_info=False):
    output_list = []
    rand_scale = random.uniform(max_downscale, 1)
    h, w, c = img_list[0].shape
    if h > w:
        crop_w = int(w * rand_scale)
        crop_h = int((crop_w / output_w) * output_h)
    else:
        crop_h = int(h * rand_scale)
        crop_w = int((crop_h / output_h) * output_w)
    # random top left coords of cropped area
    x, y = random.randint(0, h - crop_h), random.randint(0, w - crop_w)
    for img in img_list:
        img = img[x:x+crop_h, y:y+crop_w]
        img = cv2.resize(img, (output_w, output_h))
        output_list.append(img)
    if get_info:
        return output_list, rand_scale, x, y, crop_h, crop_w
    return output_list
