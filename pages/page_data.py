#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

activity_list = {
    '传统文化活动': ['劳动节快闪活动', '春节主题活动', '中秋赏月会', '国庆红色艺术节'],
    '策展艺术活动': ['气球艺术展', '艺术摄影展'],
    '自然教育活动': ['秦风瓦文', '自然课堂'],
    '体育运动活动': ['湖跑计划', '航模大赛'],
    '娱乐演出活动': ['啸雷脱口秀', '刘翔来了脱口秀'],
    '文创产品活动': ['金缘阁喜饼']
}

# 活动报名
event_registration = ['运动活动', '主题活动', '亲子活动', '促销活动', ]

# 导览列表
icon_list = ['景点', '商铺', '轻轨站', '便利店', '自贩机', '花车', '卫生间', '闲栖阁', '客服中心', '运动健身', '儿童娱乐', '停车场']


if __name__ == '__main__':
    print(activity_list)
