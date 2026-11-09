#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   planner.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adrian <adrian@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/06 12:04:51 by adrian              #+#    #+#            #
#   Updated: 2026/11/09 21:39:57 by adrian             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def correct_steps(lst_rutes: list[Route], parks_dict: dict[str, Park]) -> list[Route]:
    for route in lst_rutes:
        step_coutner: int = 0
        for current_park in route.path:
            next_park: Park = c
            if current_park.end:
                continue
            elif current_park.zone == "normal" or current_park.zone == "priority":
                step_coutner += 1
                
            elif current_park.zone == "restricted":
                step_coutner += 2
        route.min_steps = step_coutner

def do_the_plan(lst_rutes: list[Route], drones: list[Drone]) -> list[Plan]:
    lst_plans: list[Plan] = []
    assignment: list[int] = [0] * len(lst_rutes)
    def distribute_drones(rute_index: int, drones_remaining: int):
        if rute_index == len(lst_rutes):
            assignment[rute_index] = drones_remaining
            plan = Plan(id=len(lst_plans), rutes=lst_rutes.copy(), turns=0, drones=drones.copy())
            lst_plans.append(plan)
        else:
            for i in range(1, drones_remaining + 1):
                assignment[rute_index] = i
                distribute_drones(rute_index + 1, drones_remaining - i)
                assignment[rute_index] = 0
    if len(lst_rutes) > 0:
        distribute_drones(0, len(drones))
    return lst_plans


def plan_generator(lst_rutes: list[Route], drones: list[Drone], lst_plans: list[Plan]):
    as
