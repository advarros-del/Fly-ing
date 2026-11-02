#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   fly-in.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adrian <adrian@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/02 13:35:26 by adrian              #+#    #+#            #
#   Updated: 2026/11/02 21:08:55 by adrian             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from parser import parser, parse_obj,Parser, circuit_map, chek_circuit

def main():
    i: int = 0
    the_list: list = []
    with open ("input.txt", "r")as file:
        for line in parser(file):
            the_list.append(parse_obj(line, i))
            i += 1
    file.close()
    checker_map: list[Parser] = circuit_map(the_list)
    chek_circuit(checker_map)
    lst_drones: list[Drone] = []
    for i in range(checker_map[0].ndrones):
        lst_drones.append(Drone(checker_map[0].int(name)))
    lst_streets: list[Street] = []
    for i in range(len(checker_map)):
        if checker_map[i].thing == 'connection':
            lst_streets.append(Street(checker_map[i].name, checker_map[i].line))
    lst_parks: list[Park] = set_hubs(checker_map)
    parks_dict: dict[str, Park] = {}
    for park in lst_parks:
        parks_dict[park.name] = park


if __name__ == "__main__":
    main()
                