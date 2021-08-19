import copy
import cv2 as cv
from utils import convert

if __name__ == '__main__':
    """
    使用说明：
        修改img_path 选择自定义图片
        修改content为自定义内容
        按住鼠标左键开始画框，松开左键会显示内容所在的位置(write_content方法中可以选择是否显示矩形框)，按下q键退出
        按下右击并按任意键可重新画框
    
    """

    # 获得要放置文字的矩形
    # 知道自己要放置的子的个数
    # 按照1:字个数 找矩形，两种可能
    # # 按照矩形长为长边比例
    # # 按照矩形的短边比例
    # 计算文字宽度的像素值，并转换为字号
    # 求坐标
    param = [[], [], False]
    img_path = "images/pyq2.png"
    image = cv.imread(img_path)
    window_name = "rectangle"
    content = "机器人爱好者协会"
    cv.namedWindow(window_name)
    cv.imshow(window_name, image)
    cv.waitKey(1)
    cv.setMouseCallback(window_name, convert.on_mouse_action, param)
    while True:
        print(param)
        new_image = copy.deepcopy(image)
        if param[0] and param[1]:
            cv.rectangle(new_image, param[0], param[1], (255, 0, 0), 2)
        cv.imshow(window_name, new_image)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        if param[2]:
            new_image = convert.write_content(content, param[0], param[1], copy.deepcopy(image))
            cv.imshow(window_name, new_image)
            if cv.waitKey(0) & 0xFF == ord('q'):
                break

    cv.destroyAllWindows()
