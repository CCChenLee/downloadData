#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#现在pygal已经没有i18n模块，要改用pygal_maps_world.i18n
from pygal_maps_world.i18n import COUNTRIES
"""
Pygal中的地图制作工具要求数据为特定的格式：
用国别码表示国家，以及用数字表示人口数量。
Pygal使用的国别码存储在模块i18n （internationalization的缩写）中。
字典COUNTRIES 包含的键和值分别为两个字母的国别码和国家名。
"""
for country_code in sorted(COUNTRIES.keys()):
	print(country_code,COUNTRIES[country_code])