#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   parser.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adrian <adrian@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/29 20:18:35 by adrian              #+#    #+#            #
#   Updated: 2026/10/31 14:52:35 by adrian             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from io import TextIOWrapper

class Parser:
    def __init__(self, thing:str, name:str, line:int, coord_x :int, coord_y:int, metadata:str,):
        self.thing = thing
        self.name = name
        self.line = line
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.metadata = metadata
        self.ndrones = 0


def parser(file: TextIOWrapper) -> str:
    for line in file.readlines():
        if line.strip() == '':
            continue
        yield line.strip()
        if line[0] is ' ':
            raise ValueError("Invalid input: line cannot start with a space")
        line = line.strip()
        if multiple_spaces(line):
            raise ValueError("Invalid input: line cannot have multiple spaces between words")
        return line

def multiple_spaces(line: str) -> bool:
    prev_sapce: bool = False
    for char in line:
        if char == ' ':
            if prev_sapce:
                return True
            prev_sapce = True
        else:
            prev_sapce = False
    return False
        
        
def parse_obj(line: str) -> Parser:
    the_list: list[str] = line.split(' ')
    if the_list[1] == '0' and len(the_list) == 3:
        name:str = the_list[0]
        line:int = int(the_list[1])
        ndrones:int = int(the_list[2])
        return Parser(name, line, 0, 0, '', ndrones)
    elif not the_list[1] == '0' and len(the_list) == 5: 
        raise ValueError("Invalid input: not right format")
    else:
        name: str = the_list[0]
        line: int = int(the_list[1])
        coord_x: int = int(the_list[2])
        coord_y: int = int(the_list[3])
        metadata: str = the_list[4]
        return Parser(name, line, coord_x, coord_y, metadata)

def circuit_map(input_file: list[str]) -> list[Parser]:
    circuit: list[Parser] = []
    for line in input_file:
        circuit.append(parse_obj(line))
    return circuit

def check_circuit(circuit: list[Parser]) -> None:
    try:
        for obj in circuit:
            if obj.line == 0 and obj.ndrones == 0:
                raise ValueError("Invalid input: line 0 must have drones")
            if obj.line != 0 and obj.ndrones != 0:
                raise ValueError("Invalid input: line not 0 cannot have drones")
            if obj.thing not in ["nb_drones", "start_hub", "end_hub", "drone", "connection"]:
                raise ValueError(f"Invalid input: unknown object name {obj.name} in line {obj.line}")
            if obj.thing.endswith(":"):
                raise ValueError(f"Invalid input: the line {obj.line} cannot end with ':' don't have the right format")
            if int(obj.coord_x) < 0 or int(obj.coord_y) < 0:
                raise ValueError(f"Invalid input: the line {obj.line} has negative coordinates")
            if not obj.metadata.startswith("[") or not obj.metadata.endswith("]"):
                raise ValueError(f"Invalid input: the line {obj.line} has invalid metadata format")
    except ValueError as e:
        print(e)
        exit(1)
            

        
            
        