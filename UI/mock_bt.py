#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 antoni <antoni@antoni>
#
# Distributed under terms of the MIT license.

import json

info = dict()
info['notification_time'] = int(input('notification time: '))
info['breakfast_hour'] = int(input('breakfast hour: '))
info['emails'] = input('email: ')
info['dinner_hour'] = int(input('dinner hour: '))
info['breakfast_minute'] = int(input('breakfast minute: '))
info['dinner_minute'] = int(input('dinner minute: '))

'''
info = {
    "notification_time": 20,
    "breakfast_hour": 10,
    "emails": "[Alice@email.com, bob@email.com]",
    "dinner_hour": 18,
    "breakfast_minute": 0,
    "dinner_minute": 0
}
'''

with open('settings.json', 'w') as f:
    json.dump(info, f, indent=2)
