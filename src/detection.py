from paddleocr import PaddleOCR,draw_ocr
import sys

# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=False, lang='ch') # need to run only once to download and load model into memory
img_path = '../data/ppocr_img/imgs_en/wxl.png'
font_path = '../data/ppocr_img/fonts/simfang.ttf'
result = ocr.ocr(img_path, cls=True)

# for idx in range(len(result)):
#     res = result[idx]
#     for line in res:
#         print(line)

# draw result
from PIL import Image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]

for i in range(len(txts)):
    print(txts[i])

# sys.exit(0)
# im_show = draw_ocr(image, boxes, txts, scores, font_path)
# im_show = Image.fromarray(im_show)
# im_show.save('result.jpg')