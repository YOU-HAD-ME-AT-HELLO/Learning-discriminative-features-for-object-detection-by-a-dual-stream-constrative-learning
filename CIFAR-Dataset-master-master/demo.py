#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# File: demo.py


import os, cv2
from pickled import *
from load_data import *

data_path = ""
train_file_list = "data/cow_jpg_train.lst"
test_file_list = "data/cow_jpg_test.lst" #上一步生成的图片路径文件

train_save_path = "D:\\PythonMain\\2_Contrast_Learning_For_Object_Detection\\data_processing\\CIFAR-Dataset-master-master\\bin1"
test_save_path = "D:\\PythonMain\\2_Contrast_Learning_For_Object_Detection\\data_processing\\CIFAR-Dataset-master-master\\bin2"

if __name__ == '__main__':
  data, label, lst = read_data(train_file_list, data_path, shape=32)
  pickled(train_save_path, data, label, lst, bin_num = 5)#bin_num为生成的batch数量

  data, label, lst = read_data(test_file_list, data_path, shape=32)
  pickled(test_save_path, data, label, lst, bin_num=1)


