#!/usr/bin/env python

__author__ = 'Haley Collard'

import re
import json
import requests


def get_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    data = json.loads(r.text)
    # print(data)
    print(f'There are {data.get("number")} astronauts currently in space.')
    print(f'There names and crafts names are... {data.get("people")}')


def get_coordinates():
    ISS_dict = {}
    r = requests.get('http://api.open-notify.org/iss-now.json')
    data = r.text
    matches = re.findall(r'-?\d+\.?\d+', data)
    ISS_dict['timestamp'] = matches[0]
    ISS_dict['latitude'] = matches[1]
    ISS_dict['longitude'] = matches[2]
    return ISS_dict

def main():
    get_astronauts()
    # get_coordinates()


if __name__ == '__main__':
    main()
