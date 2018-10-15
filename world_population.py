#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import json
import pygal

from country_codes import get_country_code

#第一条可改变样色，第二条设置高亮的默认基色
# from pygal.style import RotateStyle
# from pygal.style import LightColorizedStyle
# from pygal.style import LightColorizedStyle,RotateStyle
from pygal.style import LightColorizedStyle as LCS,RotateStyle as RS

#将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

#打印每个国家2010年的人口数量
# for pop_dict in pop_data:
# 	if pop_dict['Year'] == '2010':
# 		country_name = pop_dict['Country Name']
# 		# population = pop_dict['Value']
# 		# 每个字符串成功转换成浮点数再转换成整数，再以数字格式存储人口数量值
# 		population = int(float(pop_dict['Value']))
# 		# print(country_name+": "+str(population))
# 		code = get_country_code(country_name)
# 		if code:
# 			print(code+": "+str(population))
# 		else:
# 			print('Error - '+country_name)

#创建一个包含人口数量的字典
#以Pygal要求的格式存储国别码和人口数量
cc_populations = {} 
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country_name)
		if code:
			#键为两个字母的国别码，值为人口数量
			cc_populations[code] = population

#根据人口数量将所有的国家分成三组
cc_pop_1,cc_pop_2,cc_pop_3 = {},{},{}
for cc,pop in cc_populations.items():
	if pop<100000000:
		cc_pop_1[cc]=pop
	elif pop<1000000000:
		cc_pop_2[cc]=pop
	else:
		cc_pop_3[cc]=pop
#看看每组分别包含多少个国家
print(len(cc_pop_1),len(cc_pop_2),len(cc_pop_3))

# wm_style = RotateStyle('#336699')
# wm_style = LightColorizedStyle
# wm_style = RotateStyle('#336699',base_style=LightColorizedStyle)
wm_style = RS('#336699',base_style=LCS)

wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010,by Country'
# wm.add('2010',cc_populations)
wm.add('0-10m',cc_pop_1)
wm.add('10m-1bn',cc_pop_2)
wm.add('>10bn',cc_pop_3)

wm.render_to_file('world_population.svg')