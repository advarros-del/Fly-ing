#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   set_objets.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adrian <adrian@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/02 20:08:08 by adrian              #+#    #+#            #
#   Updated: 2026/11/03 22:06:48 by adrian             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

 
def set_hubs(checker_map: list[Parser]) -> list[Park]:
    lst_parks: list[Park] = []
    aux_hub: Park = None
    for i in range(len(checker_map)):
        if checker_map[i].thing == 'start_hub':
            aux_hub.start = True
            aux_hub.name = checker_map[i].name
            aux_hub.coord_x = checker_map[i].coord_x
            aux_hub.coord_y = checker_map[i].coord_y
        elif checker_map[i].thing == 'end_hub':
            aux_hub.end = True
            aux_hub.name = checker_map[i].name
            aux_hub.coord_x = checker_map[i].coord_x
            aux_hub.coord_y = checker_map[i].coord_y
        elif checker_map[i].thing == 'hub':
                aux_hub.name = checker_map[i].name
                aux_hub.coord_x = checker_map[i].coord_x
                aux_hub.coord_y = checker_map[i].coord_y
        checker_map[i].metadata.remove('[' and ']')
        lst_metadatas: list[str] = checker_map[i].metadata.split(' ')
        for metadata in lst_metadatas:
            data: tuple[str, str] = metadata.split('=')
            if data[0] == 'zone':
                aux_hub.zone = data[1]
            elif data[0] == 'color':
                aux_hub.color = data[1]
            elif data[0] == 'max_drones':
                aux_hub.capacity = int(data[1])
            else:
                raise ValueError(f"Invalid input: unknown metadata '{data[0]}' for start_hub")
        lst_parks.append(aux_hub)
    return lst_parks

def set_streets(checker_map: list[Parser], parks_dict: dict[str, Park]) -> list[Street]:
    lst_streets: list[Street] = []
    aux_street: Street = None
    park_a: Park = None
    park_b: Park = None
    for i in range(len(checker_map)):
        if checker_map[i].thing == 'connection':
            checker_map[i].metadata = checker_map[i].metadata.strip()
            lst_things: list[str] = checker_map[i].metadata.split(' ')
            if len(lst_things) > 2:
                raise ValueError(f"Invalid input: too many metadata for connection")
            conexion: tuple[str, str] = lst_things[0].split('-')
            if conexion[0] not in parks_dict or conexion[1] not in parks_dict:
                raise ValueError(f"Invalid input: connection references unknown park(s)"
                                 f" '{conexion[0]}' or '{conexion[1]}'")
            park_a = parks_dict[conexion[0]]
            park_b = parks_dict[conexion[1]]
            aux_street = Street(park_a, park_b)
            if len(lst_things) > 1:
                lst_things[1] = lst_things[1].strip('[]')
                metadatas:tuple[str, str] = lst_things[1].split('=')
                if metadatas[0] != 'max_link_capacity' or not metadatas[1].isdigit():
                    raise ValueError(f"Invalid input: unknown metadata for connection")
                if metadatas[0] == 'max_link_capacity':
                    aux_street.capacity = int(metadatas[1])
                else:
                    raise ValueError(f"Invalid input: unknown metadata '{metadatas[0]}' for connection")
            park_a.connections.append(aux_street)
            park_b.connections.append(aux_street)
            lst_streets.append(aux_street)
    return lst_streets
    
def set_map(lst_parks: list[Park], lst_streets: list[Street], parks_dict: dict[str, Park]) -> map:
    start_hub: Park = None
    end_hub: Park = None
    for park in lst_parks:
        if park.start:
            start_hub = park
        elif park.end:
            end_hub = park
    return map(lst_parks, lst_streets, start_hub, end_hub)

def find_rutes(the_map: map) -> list[Rute]:
    lst_rutes: list[Rute] = []
    visited: set[Park] = set()
    path: list[Park] = []
    dfs(the_map.start_hub, the_map.end_hub, visited, path, lst_rutes)
    if not lst_rutes:
        raise ValueError("Invalid input: no valid routes found from start to end hub")


def dfs(current: Park, end: Park, visited: set[Park], path: list[Park], lst_rutes: list[Rute], i: int = 1) -> None:
    visited.add(current)
    path.append(current)
    if current == end:
        lst_rutes.append(Rute(f"Rute {i}", len(path), path.copy()))
        i += 1
    else:
        for street in current.connections:
            next_park: Park = None
            if street.park_a == current:
                next_park = street.park_b
            else:
                next_park = street.park_a
            if next_park.zone == "blocked" or next_park in visited:
                continue
            dfs(next_park, end, visited, path, lst_rutes, i)
    path.pop()
    visited.remove(current)
            
            
            
