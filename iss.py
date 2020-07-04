#!/usr/bin/env python

__author__ = 'Haley Collard'

import requests


def get_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    resp_list = r.text.split('[')
    number = resp_list[0].split(',')
    number = number[1]
    print(f'There are {number[-1:]} astronauts currently in space.')
    print(f'There names and crafts names are... {resp_list[1]}')


def main():
    get_astronauts()


if __name__ == '__main__':
    main()
