#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import pygal

wm = pygal.maps.world.World()
wm.title = 'Population of Countries in North America'
wm.add('North America',{'ca':99999999,'us':88888888,'mx':66666666})

wm.render_to_file('na_population.svg')