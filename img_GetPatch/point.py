import os
import json
import matplotlib.pyplot as plt
from PIL import Image
import random




def decode_json(json_floder_path, json_name):
    json_path = os.path.join(json_floder_path, json_name)
    data = json.load(open(json_path, 'r', encoding='gb2312', errors='ignore'))
    img_w = data['imageWidth']
    img_h = data['imageHeight']
    wh = [img_w, img_h]
    pointboxs = []
    for i in data['shapes']:

        if (i['shape_type'] == 'rectangle'):
            x1 = int(i['points'][0][0])
            y1 = int(i['points'][0][1])
            x2 = int(i['points'][1][0])
            y2 = int(i['points'][1][1])
            boxpoint = [x1,y1,x2,y2]
            pointboxs.append(boxpoint)
    return pointboxs, wh

def getimage(moco_image_path, mocoimage_name):
    image_path = os.path.join(moco_image_path, mocoimage_name)
    img = plt.imread(image_path)
    mocoimg = []
    mocoimg.append(img)
    return mocoimg




def image_cut_save(path, left, upper, right, lower, save_path):

    img = Image.open(path)  # 打开图像
    box = (
        left, upper, right, lower)
    roi = img.crop(box)

    # 保存截取的图片
    roi.save(save_path)


if __name__ == "__main__":

    json_floder_path = "D:\\Tools-data\\PyCharm\\Object-detection-based-on-Two\\2_Contrast_Learning_For_Object_Detection\\data_processing\\data\\json\\"    #路径
    json_names = os.listdir(json_floder_path)
    point = []
    wh = []
    for json_name in json_names:
        boxpoints, whs = decode_json(json_floder_path, json_name)
        point.append(boxpoints)
        wh.append(whs)
    moco_point = point
    moco_wh = wh

    moco_image_path = "D:\\Tools-data\\PyCharm\\Object-detection-based-on-Two\\2_Contrast_Learning_For_Object_Detection\\data_processing\\data\\image\\"
    mocoimage_names = os.listdir(moco_image_path)
    path = []
    for t in mocoimage_names:
        imagename = t
        image_path = os.path.join(moco_image_path, imagename)
        path.append(image_path)
    moco_path = path
    names = []
    for i in mocoimage_names:
        name = i[:-4]
        names.append(name)
    moco_name = names

    project = []
    num = len(mocoimage_names)
    for j in range(num):
        a = [moco_name[j], moco_point[j], moco_path[j], moco_wh[j]]
        project.append(a)
    mocoproject = project
    for k in range(num):
        old_image_path = mocoproject[k][2]
        save_classimage_path = "D:\\Tools-data\\PyCharm\\Object-detection-based-on-Two\\2_Contrast_Learning_For_Object_Detection\\data_processing\\outimage\\class\\" + str(mocoproject[k][0]) + "class.jpg"
        old_image_point = mocoproject[k][1][0]
        xc1 = old_image_point[0]
        yc1 = old_image_point[1]
        xc2 = old_image_point[2]
        yc2 = old_image_point[3]
        image_cut_save(old_image_path, xc1, yc1, xc2, yc2, save_classimage_path)

    for m in range(num):
        old_image_path = mocoproject[m][2]
        old_image_point = mocoproject[m][1][0]
        save_classimage_path = "D:\\Tools-data\\PyCharm\\Object-detection-based-on-Two\\2_Contrast_Learning_For_Object_Detection\\data_processing\\outimage\\background\\" + str(mocoproject[m][0]) + "background.jpg"
        patch_size = 32
        p = patch_size
        h = int(mocoproject[m][3][0])
        w = int(mocoproject[m][3][1])
        x1 = old_image_point[0]
        y1 = old_image_point[1]
        x2 = old_image_point[2]
        y2 = old_image_point[3]
        x = random.randrange(0, (h - p))
        y = random.randrange(0, (w - p))
        while x > x1 - p or x < x2:
            if x > x1 - p:
                if x < x2:
                    x = random.randrange(0, (h - p))
                else:
                    break
            else:
                break

        while y > y1 - p and y < y2:
            if y > y1 - p:
                if y < y2:
                    y = random.randrange(0, (w - p))
                else:
                    break
            else:
                break
        xb1 = x
        yb1 = y
        xb2 = x + p
        yb2 = y + p
        image_cut_save(old_image_path, xb1, yb1, xb2, yb2, save_classimage_path)



