#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   set_objets.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adrian <adrian@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/02 20:08:08 by adrian              #+#    #+#            #
#   Updated: 2026/11/02 21:35:08 by adrian             ###   ########.fr      #
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
    for i in range(len(checker_map)):
        if checker_map[i].thing == 'connection':
            checker_map[i].metadata.strip()
            lst_things: list[str] = checker_map[i].metadata.split(' ')
            conexion: tuple[str, str] = lst_things[0].split('-')
            aux_street = Street(conexion[0], conexion[1])
            if len(lst_things) > 1:
                lst_things[1].strip('[]')
                metadatas:tuple[str, str] = lst_things[1].split('=')
                if metadatas[0] != 'max_link_capacity' and not metadatas[1].isdigit():
                    raise ValueError(f"Invalid input: unknown metadata for connection")
                for metadata in lst_metadatas:
                    data: tuple[str, str] = metadata.split('=')
                    if data[0] == 'length':
                        aux_street.length = float(data[1])
                    elif data[0] == 'max_speed':
                        aux_street.max_speed = float(data[1])
                    else:
                        raise ValueError(f"Invalid input: unknown metadata '{data[0]}' for connection")
            aux_street.conections.append(parks_dict[conexion[0]])
            aux_street.conections.append(parks_dict[conexion[1]])
            lst_streets.append(aux_street)
    
            
            
            
