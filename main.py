# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        main
   Description:
   Author:           wyq19
   Date：            2018/10/31 0031 22:11
   Version:          python3.6
-------------------------------------------------
   Change Activity:
                     2018/10/31 0031 22:11
-------------------------------------------------
"""
__author__ = 'wyq19'

from scrapy import cmdline

cmdline.execute('scrapy crawl bilibili'.split())