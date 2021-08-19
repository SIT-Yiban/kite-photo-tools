import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def on_mouse_action(event, x, y, flags, param):
    """
    按下鼠标和键盘后的回调函数
    """
    if event == cv.EVENT_LBUTTONDOWN:
        param[0] = (x, y)
        param[1] = None

    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        param[1] = (x, y)
    elif event == cv.EVENT_LBUTTONUP:
        param[1] = (x, y)
        param[2] = True
    elif event == cv.EVENT_RBUTTONDOWN:
        param[0] = None
        param[1] = None
        param[2] = False

def cv_image_add_text(img, text, left_top, textColor=(0, 255, 0), textSize=20,
                      ttf="simsun.ttc"):
    """
    在cv2格式图片上写上内容
    ttf: 字体所在的路径，如果路径中字体不存在就在系统字体库中找
    """
    # 判断是否为opencv图片类型
    if isinstance(img, np.ndarray):
        img = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    font_text = ImageFont.truetype(ttf, textSize, encoding="utf-8")
    draw.text(left_top, text, textColor, font=font_text)
    return cv.cvtColor(np.asarray(img), cv.COLOR_RGB2BGR)


def write_content(text, left_top, bottom_right, img, font_color=(0, 0, 0), flag=0):
    """
    根据矩形区域，将文字内容自适应写在cv2格式图片上
    flag 是否显示矩形框
    """

    text_len = len(text)
    if text_len == 0:
        return
    rectangle_length = bottom_right[0] - left_top[0]
    rectangle_width = bottom_right[1] - left_top[1]
    if rectangle_length / rectangle_width >= text_len:
        font_size = rectangle_width
    else:
        font_size = int(rectangle_length / text_len)
    center = (int((bottom_right[0] + left_top[0]) / 2), int((bottom_right[1] + left_top[1]) / 2))
    font_location = (center[0] - int(font_size * text_len / 2), center[1] - int(font_size / 2))
    img = cv_image_add_text(img, text, font_location, font_color, font_size)
    if flag == 1:
        return cv.rectangle(img, left_top, bottom_right, (0, 255, 0), 2)  # 返回有框的
    elif flag == 0:
        return img
