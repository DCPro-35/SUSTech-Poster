from PIL import Image
from paddleocr import PaddleOCR,draw_ocr
import sys
import os
import json

PATH_CN = '../data/image/imgs_ch/'
PATH_EN = '../data/image/imgs_en/'
FONT_PATH = '../data/image/fonts/simfang.ttf'

def batch_ocr():

    img_dict = {}
    #read all images in the folder
    for filename in os.listdir(PATH_EN):
        if filename.endswith(".png")or filename.endswith(".jpg"):
            print(filename)
            #first 4 characters are the key
            key = filename[:4]
            img_dict[key] = ocr(PATH_EN+filename)
            print(img_dict[key])

    #save the dict to a json file
    with open('ocr_result_en.json', 'w') as fp:
        json.dump(img_dict, fp)

            # ocr = PaddleOCR(use_angle_cls=False, lang='ch')
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.

def ocr(img_path, language):
    ocr = PaddleOCR(use_angle_cls=False, lang=language) # need to run only once to download and load model into memory
    font_path = '../data/image/fonts/simfang.ttf'
    result = ocr.ocr(img_path, cls=True)
    result = result[0]
    print(result)
    return result

# def draw_result():
#     im_show = draw_ocr(image, boxes, txts, scores, font_path)
#     im_show = Image.fromarray(im_show)
#     im_show.save('result.jpg')

# batch_ocr()

# temp_path ="/root/vscode/cs330/data/image/imgs_ch/1152_真核生物为什么能穿越新元古代雪球地球事件：地球化学制约.jpg"
# ocr(temp_path, "ch")