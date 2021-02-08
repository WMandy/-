import cv2
import PIL
import string
import imageio
import numpy as np
from io import BytesIO
from PIL import ImageFile
from urllib.parse import quote
from PIL import Image, ImageSequence
from requests.exceptions import Timeout

ImageFile.LOAD_TRUNCATED_IMAGES = True

CAP_PROP_POS_MSEC = 0


def simple_image_read(img_bytes, resize=-1):
    img = cv2.imdecode(np.asarray(bytearray(img_bytes), dtype=np.uint8), cv2.IMREAD_COLOR)

    if len(img.shape) == 2:
        img = np.array([img, img, img], dtype=np.uint8).transpose((1, 2, 0))

    if img.shape[2] >= 4:
        img = img[:, :, :3]

    if resize > 0:
        img = cv2.resize(img, (resize, resize))

    return img


def load_img(request_id, url, from_disk=False, timeout=2, keep_list=True, resize=-1, interpolation=cv2.INTER_LINEAR):
    old_url = url
    try:
        # read image from url to byte buffer
        if not from_disk:
            url = quote(url, safe=string.printable)
            url = imageio.core.urlopen(url, timeout=timeout).read()

            prefix = url[:4]
            if prefix == b"RIFF":
                img = simple_image_read(url, resize=resize)
                return img, -1, 1

            frame = Image.open(BytesIO(url))
        else:
            frame = Image.open(url)

        if isinstance(frame, PIL.GifImagePlugin.GifImageFile):
            durations = []
            nframes = 0
            for a_frame in ImageSequence.Iterator(frame):
                if 'duration' not in a_frame.info:
                    durations.append(0.001)
                else:
                    durations.append(a_frame.info['duration'] / 1000)

                nframes += 1

            img = imageio.mimread(url, '.gif')

            if keep_list:
                img = list(
                    map(lambda x: np.array([x, x, x], dtype=np.uint8).transpose((1, 2, 0)) if len(x.shape) == 2 else x,
                        img))

                img = list(map(lambda x: x[:, :, :3] if x.shape[2] >= 4 else x, img))

                if resize > 0:
                    for img_idx in range(len(img)):
                        img[img_idx] = cv2.resize(img[img_idx], (resize, resize), interpolation=interpolation)

            else:
                img = np.vstack(img)

                if len(img.shape) == 2:
                    img = np.asarray([img, img, img]).astype(np.uint8)

                if img.shape[2] >= 4:
                    img = img[:, :, :3]

                if resize > 0:
                    img = cv2.resize(img, (resize, resize), interpolation=interpolation)

            return img, durations, nframes
        else:
            img = simple_image_read(url, resize=resize)
            return img, -1, 1

    except Exception as e:
        print('WARN', request_id, old_url, e)
    except Timeout:
        print('WARN', request_id, old_url, 'download timeout')
    return None, None, None
