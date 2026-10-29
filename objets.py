#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   objets.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adrian <adrian@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/29 19:42:53 by adrian              #+#    #+#            #
#   Updated: 2026/10/29 20:17:12 by adrian             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Drone:
    def __init__(self, name, model):
        self.id = id(self)
        self.steps = 0
        
class Street:
    def __init__(self, name, length):
        self.name = name
        self.capacity = capacity

class Park:
    def __init__(self, name, area):
        self.name = name
        self.capacity = capacity

class Rute:
    def __init__(self, name, length):
        self.name = name
        self.min_steps = 0
        self.path = []

class Planeer:
    def __init__(self, name):
        self.name = name
        self.rutes = []

class Simulation:
    def __init__(self, name):
        self.name = name
        self.planeers = []
