# -*- coding: utf-8 -*-
# @Time    : 2023/4/22
# @Author  : Daniel Ji

import os
from PIL import Image


def cal_avg_res():
    """
    This function calculates the average resolution (H & W) of whole dataset
    """
    root = './cos_benchmark/TestDataset'

    for data_name in os.listdir(root):
        data_root = os.path.join(root, data_name, 'GT')
        H_avg, W_avg, count = 0, 0, 0

        for file_name in os.listdir(data_root):
            img_path = os.path.join(data_root, file_name)
            img = Image.open(img_path)
            size = img.size
            H_avg += size[0]
            W_avg += size[1]
            count += 1
            
        print(f'{data_name}, H-average is {H_avg/count} and W-average is {W_avg/count}')
    