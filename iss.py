#!/usr/bin/env python

__author__ = 'Haley Collard with help from Daniel'


import time
import turtle
import requests


def get_coordinates():
    """return currant coordinates of ISS."""
    data = requests.get('http://api.open-notify.org/iss-now.json').json()
    lat = data['iss_position']['latitude']
    lon = data['iss_position']['longitude']
    return lat, lon


def set_map():
    """set up iss turtle and map screen"""
    world_map = turtle.Screen()
    iss = turtle.Turtle()
    iss.tilt(30)
    world_map.register_shape('iss.gif')
    iss.shape('iss.gif')
    world_map.setup(width=720, height=360)
    world_map.bgpic('map.gif')
    world_map.title('Currant position of the International Space Station')
    world_map.setworldcoordinates(-180.00, -90.00, 180.00, 90.00)
    iss.showturtle()
    iss.penup()
    iss.setheading(90)
    return iss, world_map


def move_iss(iss, world_map):
    """move ISS to currant location"""
    lat, lon = get_coordinates()
    lat_lon_coords = float(lon), float(lat)
    iss.setpos(lat_lon_coords)
    iss.pencolor('white')
    iss.pendown()


def over_indy():
    """plot coordinates to Indy, and set time of next pass over"""
    lon = '-86.1583502'
    lat = '39.7683331'
    indy = turtle.Turtle()
    indy.hideturtle()
    indy.penup()
    indy.setpos(float(lon), float(lat))
    indy.dot(10, "yellow")
    url = 'http://api.open-notify.org/iss-pass.json'
    params = {'lon': lon, 'lat': lat, 'n': 1}
    data = requests.get(url, params=params).json()
    risetime = time.ctime(data['response'][0]['risetime'])
    indy.color('white')
    indy.write(risetime, font=('Courier', 20, 'bold'), align='left')


def get_astronauts():
    """get a list of currant astronauts and number of people on ISS"""
    astro = turtle.Turtle()
    data = requests.get('http://api.open-notify.org/astros.json').json()
    number = data.get("number")
    peoples = data.get('people')
    a_nauts = []
    for person in peoples:
        craft = person.get('craft')
        a_nauts.append(person.get('name'))
    astro.hideturtle()
    astro.penup()
    astro.setpos(0.0, -50.0)
    astro.pencolor('yellow')
    astro.pendown()
    astro.write(f'There are {number} astronauts currently in space.',
                font=('Courier', 10, 'bold'), align='center')
    astro.penup()
    astro.setpos(0.0, -60.0)
    astro.write(f"On the craft {craft} their names are {', '.join(a_nauts)}.",
                font=('Courier', 10, 'bold'), align='center')


def main():
    iss, world_map = set_map()
    over_indy()
    get_astronauts()
    move_iss(iss, world_map)
    world_map.onkey(lambda: move_iss(iss, world_map), "space")
    world_map.listen()
    turtle.done()


if __name__ == '__main__':
    main()
