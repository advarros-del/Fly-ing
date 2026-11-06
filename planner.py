#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   planner.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adrian <adrian@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/06 12:04:51 by adrian              #+#    #+#            #
#   Updated: 2026/11/06 12:56:21 by adrian             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def correct_steps(lst_rutes: list[Route], parks_dict: dict[str, Park]) -> list[Route]:
    for route in lst_rutes:
        step_coutner: int = 0
        for current_park in route.path:
            if current_park.end:
                continue
            elif current_park.zone == "normal" or current_park.zone == "priority":
                step_coutner += 1
                
            elif current_park.zone == "restricted":
                step_coutner += 2
        route.min_steps = step_coutner
        