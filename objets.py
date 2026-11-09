#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   objets.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adrian <adrian@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/29 19:42:53 by adrian              #+#    #+#            #
#   Updated: 2026/11/09 20:32:15 by adrian             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Drone:
    def __init__(self, name, model):
        self.id = id(self)
        self.steps = 0
        
class Street:
    def __init__(self, park_a: Park, park_b: Park, capacity: int = 1):
        self.park_a: Park = park_a
        self.park_b: Park = park_b
        self.capacity: int = capacity

class Park:
    def __init__(self, name, coord_x, coord_y, capacity, color):
        self.start: bool = False
        self.end: bool = False
        self.name: str = name
        self.coord_x: int = 0
        self.coord_y: int = 0
        self.capacity: int = 1
        self.zone: str = ''
        self.color: str = ''
        self.connections: list[Street] = []

class Map:
    def __init__(self, parks, streets, start_hub, end_hub):
        self.parks: list[Park] = parks
        self.streets: list[Street] = streets
        self.start_hub: Park = start_hub
        self.end_hub: Park = end_hub

class Rute:
    def __init__(self, id, min_steps, path):
        self.id = id
        self.min_steps = min_steps
        self.path = path

class Plan:
    def __init__(self, id, rutes, turns, drones):
        self.id: int = id
        self.rutes: list[Rute] = []
        self.turns: int = turns
        self.drones: list[Drone] = []

class Simulation:
    def __init__(self, name, planeers):
        self.name = name
        self.planeers = []
