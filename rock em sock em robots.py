def fight(robot_1, robot_2, tactics):
    robot_1_health = robot_1['health']
    robot_2_health = robot_2['health']

    print(robot_1)   
    print(robot_2)

    if robot_1['tactics'] == [] and robot_2['tactics'] == []:
        return "The fight was a draw."
    elif robot_1['tactics'] == []:
        turnLen = len(robot_2['tactics'])
    elif robot_2['tactics'] == []:
        turnLen = len(robot_1['tactics'])
    elif len(robot_1['tactics']) == len(robot_2['tactics']):
        turnLen = len(robot_1['tactics'])
    elif len(robot_1['tactics']) > len(robot_2['tactics']):
        turnLen = len(robot_1['tactics'])
    else:
        turnLen = len(robot_2['tactics'])
    

    if robot_2['speed'] > robot_1['speed']:
        for i in range(turnLen):  
            if i < len(robot_2['tactics']):         
                robot_1_health -= tactics[robot_2['tactics'][i]]
                if robot_1_health <= 0:
                    return f"{robot_2['name']} has won the fight."
            if i < len(robot_1['tactics']):
                robot_2_health -= tactics[robot_1['tactics'][i]]
                if robot_2_health <= 0:
                    return f"{robot_1['name']} has won the fight."
       
    else:
        for i in range(turnLen):           
            if i < len(robot_1['tactics']):
                robot_2_health -= tactics[robot_1['tactics'][i]]
                if robot_2_health <= 0:
                    return f"{robot_1['name']} has won the fight."
            if i < len(robot_2['tactics']):         
                robot_1_health -= tactics[robot_2['tactics'][i]]
                if robot_1_health <= 0:
                    return f"{robot_2['name']} has won the fight."

    if robot_1_health == robot_2_health:
        return "The fight was a draw."
    elif robot_1_health > robot_2_health:
        return f"{robot_1['name']} has won the fight."
    else:
        return f"{robot_2['name']} has won the fight."  






robot_1 = {'name': 'Rocky', 'health': 100, 'speed': 20, 'tactics': []}
robot_2 = {'name': 'Missile Bob', 'health': 100, 'speed': 21, 'tactics': ['missile', 'missile', 'missile', 'missile']}
tactics = {"punch": 20, "laser": 30, "missile": 35}
print(fight(robot_1, robot_2, tactics))

robot_1 = {"name": "Rocky", "health": 200, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
tactics = {"punch": 20, "laser": 30, "missile": 35}
print(fight(robot_1, robot_2, tactics))

#def fight(robot_1, robot_2, tactics):
#    attack, defend = (robot_1, robot_2) if robot_1['speed'] >= robot_2['speed'] else (robot_2, robot_1)
#    
#    while attack['health'] > 0:
#        if attack['tactics']:
#            defend['health'] -= tactics[attack['tactics'].pop()]
#        elif not defend['tactics']:
#            break
#        attack, defend = defend, attack
#
#    if attack['health'] == defend['health']:
#        return "The fight was a draw."
#    return "{} has won the fight.".format((defend if attack['health'] < defend['health'] else attack)['name'])