# 读到配置文件
# 参数是 内容 图片路径
# 按照配置文件中的图片名称进行选择写字
import argparse
import os

import cv2
from utils import convert

import toml


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config-file', default='config.toml', type=str, help='photo locate config')
    parser.add_argument('--source', required=True, type=str, help='image-path')
    parser.add_argument('--content', required=True, type=str, help='association name')
    parser.add_argument('--result',default='result/',type=str,help='add content photo path')
    return parser.parse_args()


if __name__ == '__main__':
    opt = parse_opt()
    config_name = opt.config_file
    image_path = opt.source
    content = opt.content
    toml_file = toml.load(config_name)
    file_name = os.path.basename(image_path)
    if os.path.exists(image_path):
        key = os.path.splitext(file_name)[0]
        value = toml_file.get(key)
        if value :
            print(value)
            image = cv2.imread(image_path)
            image = convert.write_content(content, value['rect']['left_top'], value['rect']['right_bottom'], image)
            cv2.imwrite(opt.result+file_name, image)
        else:
            print("该图片没有被配置")
    else:
        print("文件不存在")
