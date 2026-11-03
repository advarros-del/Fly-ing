#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   objets.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adrian <adrian@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/29 19:42:53 by adrian              #+#    #+#            #
#   Updated: 2026/11/03 21:13:36 by adrian             ###   ########.fr      #
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

class map:
    def __init__(self, name, parks, streets):
        self.parks: list[Park] = []
        self.streets: list[Street] = []
        self.start_hub: Park = None
        self.end_hub: Park = None

class Rute:
    def __init__(self, name, min_steps, path):
        self.name = name
        self.min_steps = 0
        self.path = []

class Planeer:
    def __init__(self, name, rutes):
        self.name = name
        self.rutes = []

class Simulation:
    def __init__(self, name, planeers):
        self.name = name
        self.planeers = []
