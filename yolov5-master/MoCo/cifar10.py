import numpy as np
from PIL import Image
import pickle
import os
import matplotlib.image as plimg

CHANNEL = 3
WIDTH = 32
HEIGHT = 32

data = []
labels = []
classification = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

for i in range(5):
    with open("./data_processing/cifar-10-batches-py/data_batch_" + str(i + 1), mode='rb') as file:
        # 数据集在当脚本前文件夹下
        data_dict = pickle.load(file, encoding='bytes')
        data += list(data_dict[b'data_processing'])
        labels += list(data_dict[b'labels'])

img = np.reshape(data, [-1, CHANNEL, WIDTH, HEIGHT])

# 代码创建文件夹，也可以自行创建
data_path = "./dataimg/img/"
if not os.path.exists(data_path):
    os.makedirs(data_path)

for i in range(100):
    r = img[i][0]
    g = img[i][1]
    b = img[i][2]

    plimg.imsave("./dataimg/rgb/" + str(i) + "r" + ".png", r)
    plimg.imsave("./dataimg/rgb/" + str(i) + "g" + ".png", g)
    plimg.imsave("./dataimg/rgb/" + str(i) + "b" + ".png", b)

    ir = Image.fromarray(r)
    ig = Image.fromarray(g)
    ib = Image.fromarray(b)
    rgb = Image.merge("RGB", (ir, ig, ib))

    name = "img-" + str(i) + "-" + classification[labels[i]] + ".png"
    rgb.save(data_path + name, "PNG")

