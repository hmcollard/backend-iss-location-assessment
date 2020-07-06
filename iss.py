#!/usr/bin/env python

__author__ = 'Haley Collard'


import json
import time
import turtle
import requests


def get_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    data = json.loads(r.text)
    print(f'There are {data.get("number")} astronauts currently in space.')
    print(f'There names and crafts names are... {data.get("people")}')


def get_coordinates():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    data = json.loads(r.text)
    return data


def set_map():
    world_map = turtle.Screen()
    iss = turtle.Turtle()
    iss.tilt(30)
    world_map.register_shape('iss.gif')
    iss.shape('iss.gif')
    world_map.setup(width=.6, height=.5, startx=None, starty=None)
    world_map.bgpic('map.gif')
    world_map.title('Currant position of the International Space Station')
    world_map.setworldcoordinates(-180.00, -90.00, 180.00, 90.00)
    iss.showturtle()
    iss.penup()
    # iss.setheading(90)
    # world_map.onkey(move_iss(iss, world_map), "space")
    # world_map.listen()
    return iss, world_map


def move_iss(iss, world_map):
    coords = get_coordinates()
    lat = coords['iss_position']['latitude']
    lon = coords['iss_position']['longitude']
    lat_lon_coords = float(lon), float(lat)
    iss.setpos(lat_lon_coords)
    iss.pencolor('white')
    iss.pendown()
    world_map.exitonclick()


def over_indy():
    lon = '-86.1583502'
    lat = '39.7683331'
    indy = turtle.Turtle()
    indy.hideturtle()
    indy.penup()
    indy.setpos(float(lon), float(lat))
    indy.dot(10, "yellow")
    url = 'http://api.open-notify.org/iss-pass.json'
    payload = {'longitude': lon, 'latitude': lat}
    # r = requests.get(url, params=payload)
    # data = json.loads(r.text)
    # timestamp = time.ctime(data.get('timestamp'))
    # print(timestamp)


def main():
    get_astronauts()
    iss, world_map = set_map()
    over_indy()
    move_iss(iss, world_map)


if __name__ == '__main__':
    main()
