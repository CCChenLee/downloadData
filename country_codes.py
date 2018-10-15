#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
	"""根据指定的国家，
	返回Pygal使用的两个字母的国别码
	作为函数使用
	"""
	for code,name in COUNTRIES.items():
		if name == country_name:
			return code

		if country_name == 'Yemen, Rep.':
			return 'ye'
	#如果没有找到指定的国家，就返回None
	return None

# print(get_country_code('China')) # cn
# print(get_country_code('America')) # None
# print(get_country_code('France')) # fr

# def main():
# 	get_country_code()

# if __name__ =="__main__":
# 	main()