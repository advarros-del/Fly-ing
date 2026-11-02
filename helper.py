#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   helper.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adrian <adrian@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/02 18:47:01 by adrian              #+#    #+#            #
#   Updated: 2026/11/02 20:50:46 by adrian             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def Check_unique_name(checker_map: list[Parser]):
    names: set[str] = set()
    for obj in checker_map:
        if obj.name in names:
            raise ValueError(f"Invalid input: duplicate name '{obj.name}' found")
        names.add(obj.name)

def Check_unique_coordinates(checker_map: list[Parser]):
    coordinates: set[tuple[int, int]] = set()
    for obj in checker_map:
        coord = (obj.coord_x, obj.coord_y)
        if coord in coordinates:
            raise ValueError(f"Invalid input: duplicate coordinates {coord} found")
        coordinates.add(coord)

def Check_unique_start_end(checker_map: list[Parser]):
    start_count = 0
    end_count = 0
    for obj in checker_map:
        if obj.thing == 'start_hub':
            start_count += 1
        elif obj.thing == 'end_hub':
            end_count += 1
    if start_count != 1:
        raise ValueError(f"Invalid input: there must be exactly one start point, found {start_count}")
    if end_count != 1:
        raise ValueError(f"Invalid input: there must be exactly one end point, found {end_count}")

def every_rute_has_start_and_end(lst_parks, lst_streets):
    start_hub: Park = None
    end_hub: Park = None
    for park in lst_parks:
        if park.start:
            start_hub = park
        elif park.end:
            end_hub = park
    if not start_hub or not end_hub:
        raise ValueError("Invalid input: there must be exactly one start and one end hub")
