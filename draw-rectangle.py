import copy
import os

import toml
import cv2 as cv

from utils import convert

if __name__ == '__main__':
    config_file = 'config.toml'
    param = [[], [], False]
    image_path = 'images/pyq3.png'
    image = cv.imread(image_path)
    window_name = 'rectangle'
    cv.imshow(window_name, image)
    cv.waitKey(1)
    cv.setMouseCallback(window_name, convert.on_mouse_action, param)
    while True:
        new_image = copy.deepcopy(image)
        if param[0] and param[1]:
            cv.rectangle(new_image, param[0], param[1], (255, 0, 0), 2)
        cv.imshow(window_name, new_image)
        if cv.waitKey(1) & 0xFF == ord('q'):
            toml_file = toml.load(config_file)
            file_name = os.path.basename(image_path)
            key = os.path.splitext(file_name)[0]
            value = {
                "name": file_name,
                "font": "simsun.ttc",
                "color": (0, 0, 0),
                "rect": {
                    "left_top": param[0],
                    "right_bottom": param[1]
                }
            }
            toml_file.update({key:value})
            with open(config_file, 'w') as f:
                print(toml_file)
                toml.dump(toml_file, f)
            break
    cv.destroyAllWindows()
