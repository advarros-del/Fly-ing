#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   planner.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adrian <adrian@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/06 12:04:51 by adrian              #+#    #+#            #
#   Updated: 2026/11/13 20:15:44 by adrian             ###   ########.fr      #
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

def plan_generator(lst_rutes: list[Route], drones: list[Drone]) -> list[Plan]:
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


def simualtion(plan: Plan) -> Plan:
    plan_backup: Plan = plan
    turns: int = 0
    priority_rules: dict[str, int] = {"priority": 1, "normal": 2, "restricted": 2}
    for drone in plan.drones:
        if drone.position is None:
            drone.position = plan.rutes[drone.rute.id].path[0]
        if drone.rute is None:
            for asignation in plan_backup.asignments:
                if asignation[0] > 0:
                    drone.rute = plan.rutes[asignation[1]]
                    asignation[0] -= 1
                    break
                else:
                    continue
    while (len(plan.drones_finished) < len(plan.drones)):
        priority_parks_turn: list[Park] =  []
        movements_this_turn: list[tuple[Drone, Park]] = []
        plan.drones.sort(key=lambda d: (priority_rules[d.next_park.zone], d.id))
        turns += 1
        for drone in plan.drones:
            if drone not in plan.drones_finished:
                if drone.position == drone.next_park:
                    if drone.position == drone.rute.path[-1]:
                        drone.finished = True
                        plan.drones_finished.append(drone)
                    else:
                        drone.next_park = drone.rute.path[drone.rute.path.index(drone.position) + 1]
            elif drone.finished:
                continue
            for street in drone.position.connections:
                if street.park_a == drone.position:
                    next_park = street.park_b
                else:
                    next_park = street.park_a
                if next_park.zone == "priority":
                    priority_parks_turn.append(next_park)
            if drone.next_park.capacity > 0 and drone.next_park.zone in ["priority", "normal"]:
                drone.position = drone.next_park
                drone.next_park.capacity -= 1
            elif drone.next_park.zone == "restricted":
                if drone.next_park.capacity > 0:
                    for street in drone.position.connections:
                        if street.park_a == drone.position:
                            next_park = street.park_b
                        else:
                            next_park = street.park_a
                        if next_park == drone.next_park:
                            drone.
                    drone.next_park.capacity -= 1
                else:
                    continue
            else:
                continue
                    
    if plan.drones_finished != len(plan.drones):
        plan.valid = False
    return plan 
        
            
    