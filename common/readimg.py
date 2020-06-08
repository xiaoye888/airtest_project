#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import os
from config import conf


class ReadImg(object):
    def __init__(self, name):
        self.path = os.path.join(conf.AIR_IMG_PATH, name)

    def __getitem__(self, item):
        result = os.path.join(self.path, "{}.png".format(item))
        if os.path.isfile(result):
            return result
        raise FileNotFoundError("{}不存在".format(result))


index_img = ReadImg('index')
my_img = ReadImg('my')
act_img = ReadImg('activity')
icon_img = ReadImg('guide')

__all__ = ['index_img', 'my_img', 'act_img', 'icon_img']

if __name__ == '__main__':
    pass
