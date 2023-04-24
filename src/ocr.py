from PIL import Image
from paddleocr import PaddleOCR,draw_ocr
import sys
import os
import json

PATH_CN = '../data/ppocr_img/imgs_ch/'
PATH_EN = '../data/ppocr_img/imgs_en/'
FONT_PATH = '../data/ppocr_img/fonts/simfang.ttf'

def batch_ocr():

    img_dict = {}
    #read all images in the folder
    for filename in os.listdir(PATH_CN):
        if filename.endswith(".png")or filename.endswith(".jpg"):
            print(filename)
            #first 4 characters are the key
            key = filename[:4]
            img_dict[key] = ocr(PATH_CN+filename)
            print(img_dict[key])

    #save the dict to a json file
    with open('ocr_result.json', 'w') as fp:
        json.dump(img_dict, fp)

            # ocr = PaddleOCR(use_angle_cls=False, lang='ch')
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.

def ocr(img_path):
    ocr = PaddleOCR(use_angle_cls=False, lang='ch') # need to run only once to download and load model into memory
    font_path = '../data/ppocr_img/fonts/simfang.ttf'
    result = ocr.ocr(img_path, cls=True)
    result = result[0]
    return result


# def draw_result():
#     im_show = draw_ocr(image, boxes, txts, scores, font_path)
#     im_show = Image.fromarray(im_show)
#     im_show.save('result.jpg')


