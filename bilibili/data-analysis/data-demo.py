# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        demo
   Description:
   Author:           wyq19
   Date：            2018/11/3 0003 9:47
   Version:          python3.6
-------------------------------------------------
   Change Activity:
                     2018/11/3 0003 9:47
-------------------------------------------------
"""
__author__ = 'wyq19'
import pandas as pd
from pyecharts import Pie,Line,Scatter
import os
import numpy as np
import jieba
import jieba.analyse
from wordcloud import WordCloud,ImageColorGenerator
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from datetime import datetime

datas = pd.read_table(open('bilibili.txt', encoding='utf8'))

del datas['id']
del datas['time']

scores = datas.rating.groupby(datas['rating']).count()
# print(scores.index.values)
pie = Pie('《工作细胞》用户评分')
pie.add(
    '',
    ['1星', '2星', '3星', '4星', '5星'],# scores.index.values,
    scores.values,
    center=[50,60],
    is_label_show=True,
)
pie.render('评分.html')

datas['dates'] = datas.ctime.apply(lambda x:pd.Timestamp(datetime.fromtimestamp(x)).date())
num_date = datas.mid.groupby(datas['dates']).count()
line1 = Line('评论数时间分布')
line1.use_theme('dark')
line1.add(
    '',
    num_date.index.values,
    num_date.values,
    is_fill=True,
)
line1.render('评论数时间分布.html')

datas['times'] = datas.ctime.apply(lambda x:pd.Timestamp(datetime.fromtimestamp(x)).time().hour)
num_time = datas.mid.groupby(datas['times']).count()
line2 = Line('评论数日内分布')
line2.use_theme('dark')
line2.add(
    '',
    num_time.index.values,
    num_time.values,
    is_label_show=True,
    mark_point_symbol='diamond', mark_point_textcolor='#40ff27',
    line_width = 2
)
line2.render('评论数日内分布.html')